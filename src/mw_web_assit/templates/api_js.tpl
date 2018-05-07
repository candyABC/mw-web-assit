import axios from 'axios'
//import {convert_query_params} from './util'
const isProduction = process.env.NODE_ENV === "production"
//const root_uri =isProduction?'http://112.74.169.245/kong':'../..'
const root_uri =''
export const {{ apimethods.baseuriName }}=root_uri+'{{ apimethods.basePath }}'

{% for method in apimethods.methods %}

export const {{ method.opId }}=({{ method.paramArgs }})=>{
    {% if method.queryParams|length>0 %}
    let queryParamsStr =convert_query_params(queryParam)
    /* queryParam:
    {
        {% for param in method.queryParams %}
        {{ param.name }} {{ param.type }}  required:{{ param.required }}
        {% endfor %}    }*/

    {% endif %}
    return axios.{{ method.name }}(`{{ method.uri }}{% if method.queryParams|length>0 %}${queryParamsStr}{% endif %}`{% if method.dataParam %},dataParam{% endif %}
        {% if method.paramXtype==1 %},{headers: {'enctype': 'multipart/form-data','Content-Type': 'multipart/form-data'}}{% endif %}
        {% if method.paramXtype==2 %},{headers: {'Content-Type': 'application/x-www-form-urlencoded'}{% endif %})
}

{% endfor %}