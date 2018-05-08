import yaml,os
from .templates import api_js,class_assit
def read_swagger(filename):
    with open(filename,encoding='utf-8') as f:
        return yaml.load(f)

class ApiMethod():
    def __init__(self,name,opId,uri,params):
        self.name =name
        self.opId =opId
        self.uri =uri
        # self.method =method
        self.params =params or []
        self.parseArgs()
        # self.queryParams =[]
        # self.dataParams = []
        # self.paramArgs =''
    @property
    def paramXtype(self):
        # paramXtype: 0 default, 1 formdata,2 file ,根据paramXtype的类型决定header传什么content-type
        def has_param_in(in_type):
            return next((param for param in self.params if param.get('in') == in_type), None) is not None

        if has_param_in("formData"):
            return 1
        elif has_param_in("file"):
            return 2
        else:
            return 0



    def parseArgs(self):
        # 仅对 param in 是 path,query的做处理,required =false 的设定null
        args=','.join([param["name"] for param in self.params if param.get("in") =='path'])
        self.queryParams =[param for param in self.params if param.get("in") =='query']
        self.dataParams =[param for param in self.params if param.get("in") in("body","formData","file")]

        if len(self.queryParams)>0:
            if len(args)>0:
                args+=','
            args += 'queryParam'
        if len(self.dataParams)>0:
            if len(args)>0:
                args+=','
            args+= 'dataParam'


        self.paramArgs =args

def save_file(txt,filename):
    with open(filename,mode='w',encoding='utf-8') as f:
        f.write(txt)

class SwProp():
    def __init__(self,name,xtype,description,default):
        self.name=name
        self.description=description
        self.xtype=xtype
        self.default =default or self.guess_default()


    def guess_default(self):
        (_type, _format) = self.xtype
        if _type in ('integer','float'):
            return 0
        elif _type in ('boolean'):
            return False
        else:
            return "''"

    @property
    def ruleType(self):
        (_type,_format)=self.xtype
        if _type=='string':
            if _format =='date':
                return 'date'
            elif _format =='date-time':
                return 'time'
            else:
                return None

class SwObject():
    def __init__(self,name,description):
        self.name =name
        self.description=description
        self.props =[]
    def createProp(self,name,xtype,description,default):
        return self.props.append(SwProp(name,xtype,description,default))

class ApiMethods():
    def __init__(self):
        self.methods =[]

    def parse(self,swagger):
        self.methods.clear()
        self.basePath = swagger.get('basePath')
        self.baseuriName = '_'.join(self.basePath.replace('.', '').split('/')).strip('_')
        for pathName, methods in swagger['paths'].items():
            for methodName, method in methods.items():
                apimethod = ApiMethod(methodName,
                                      method['operationId'].split('.')[-1],
                                      '${%s}%s' % (self.baseuriName, pathName.replace('{', '${')),
                                      method.get("parameters")
                                      )
                apimethod.summary =method.get("summary")
                self.methods.append(apimethod)

class SwaggerHelper():
    def __init__(self,inFile):
        self.swagger = read_swagger(inFile)

    def classAssit(self,outFile):
        objects =[]
        #get definiations
        for name,obj in self.swagger.get("definitions").items():

            swobj =SwObject(name,obj.get('description'))
            for propname,prop in obj.get('properties').items():
                # if not prop.get('required', False):
                #     continue
                swobj.createProp(propname,
                                 (prop['type'],prop.get('format')),
                                 prop.get('description',''),
                                 prop.get('default'))
                # swprop.isRequired = prop.get('required',False)
            objects.append(swobj)
        #todo: get query for each path
        save_file(class_assit(objects), outFile)
        # return objects

    def genApi(self,outFile):
        apimethods =ApiMethods()
        apimethods.parse(self.swagger)
        save_file(api_js(apimethods), outFile)

    def gen(self,outpath,name):
        self.genApi(os.path.join(outpath,'%s_api.js' % name))
        self.classAssit(os.path.join(outpath,'%s_assit.js' % name))



