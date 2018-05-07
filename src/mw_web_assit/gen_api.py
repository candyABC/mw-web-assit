import yaml
from .templates import api_js
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

class ApiMethods():
    def __init__(self):
        self.methods =[]

    def _inner_parse(self,swagger):
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

    def parse(self,inFile,outFile):
        swagger = read_swagger(inFile)
        self._inner_parse(swagger)
        save_file(api_js(self),outFile)

