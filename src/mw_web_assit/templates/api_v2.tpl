import {mwRequest} from "../utils/mwRequest";
const isProduction = process.env.NODE_ENV === "production"
//const root_uri =isProduction?'http://112.74.169.245/kong':'../..'
const root_uri =''
export const {{ apimethods.baseuriName }}=root_uri+'{{ apimethods.basePath }}'

{% for method in apimethods.methods %}
/* {{ method.summary }}
    {% if method.queryParams|length>0 %}
    query:
    {
        {% for param in method.queryParams %}
        {{ param.name }} {{ param.type }}  required:{{ param.required }}
        {% endfor %}    }
    {% endif %}*/
export const {{ method.opId }}=({% if method.pathArgs|length>0 %}{{ method.pathArgs }},{% endif %}params={})=>{
    params.method='{{ method.name }}'
    {% if method.paramXtype==1 %}params.header= {'enctype': 'multipart/form-data','Content-Type': 'multipart/form-data'}{% endif %}
    {% if method.paramXtype==2 %}params.header={'Content-Type': 'application/x-www-form-urlencoded'}{% endif %}
    return mwRequest(`{{ method.uri }}`,params)
}

{% endfor %}