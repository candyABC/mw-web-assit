from jinja2 import FileSystemLoader,Environment
import os


TemplatePath = os.path.dirname(__file__)
# print(TemplatePath)

# print('templatepath:%s' % TemplatePath)
load = FileSystemLoader([TemplatePath])
templateEnv =Environment(loader=load)
templateEnv.trim_blocks = True
templateEnv.lstrip_blocks = True

def api_js(apiMethods):
    t = templateEnv.get_template('api_js.tpl')
    return t.render(apimethods =apiMethods)

def class_assit(objects):
    t = templateEnv.get_template('class_assit.tpl')
    return t.render(objects =objects)