import axios from 'axios'
//import {convert_query_params} from './util'
const isProduction = process.env.NODE_ENV === "production"
//const root_uri =isProduction?'http://112.74.169.245/kong':'../..'
const root_uri =''
export const _gongdi_mng_v10=root_uri+'/gongdi_mng/v1.0'


export const emp_illegals_get=(queryParam)=>{
    let queryParamsStr =convert_query_params(queryParam)
    /* queryParam:
    {
        page integer  required:False
        per_page integer  required:False
    }*/

    return axios.get(`${_gongdi_mng_v10}/emp_illegals${queryParamsStr}`)
}


export const emp_illegals_post=(dataParam)=>{
    return axios.post(`${_gongdi_mng_v10}/emp_illegals`)
}


export const emp_illegals_id_get=(id)=>{
    return axios.get(`${_gongdi_mng_v10}/emp_illegals/${id}`)
}


export const emp_illegals_id_put=(id,dataParam)=>{
    return axios.put(`${_gongdi_mng_v10}/emp_illegals/${id}`)
}


export const emp_illegals_id_delete=(id)=>{
    return axios.delete(`${_gongdi_mng_v10}/emp_illegals/${id}`)
}


export const illegal_categorys_get=()=>{
    return axios.get(`${_gongdi_mng_v10}/illegal_categorys`)
}


export const illegal_categorys_post=(dataParam)=>{
    return axios.post(`${_gongdi_mng_v10}/illegal_categorys`)
}


export const illegal_categorys_id_get=(id)=>{
    return axios.get(`${_gongdi_mng_v10}/illegal_categorys/${id}`)
}


export const illegal_categorys_id_put=(id,dataParam)=>{
    return axios.put(`${_gongdi_mng_v10}/illegal_categorys/${id}`)
}


export const illegal_categorys_id_delete=(id)=>{
    return axios.delete(`${_gongdi_mng_v10}/illegal_categorys/${id}`)
}


export const illegal_pics_post=(dataParam)=>{
    return axios.post(`${_gongdi_mng_v10}/illegal_pics`,{headers: {'enctype': 'multipart/form-data','Content-Type': 'multipart/form-data'}})
}


export const illegal_pics_id_get=(id)=>{
    return axios.get(`${_gongdi_mng_v10}/illegal_pics/${id}`)
}


export const illegal_pics_id_delete=(id)=>{
    return axios.delete(`${_gongdi_mng_v10}/illegal_pics/${id}`)
}


export const illegal_id_pics_get=(id)=>{
    return axios.get(`${_gongdi_mng_v10}/illegal/${id}/pics`)
}


export const illegal_categorys_id_types_get=(id)=>{
    return axios.get(`${_gongdi_mng_v10}/illegal_categorys/${id}/types`)
}


export const illegal_types_post=(dataParam)=>{
    return axios.post(`${_gongdi_mng_v10}/illegal_types`)
}


export const illegal_types_id_get=(id)=>{
    return axios.get(`${_gongdi_mng_v10}/illegal_types/${id}`)
}


export const illegal_types_id_put=(id,dataParam)=>{
    return axios.put(`${_gongdi_mng_v10}/illegal_types/${id}`)
}


export const illegal_types_id_delete=(id)=>{
    return axios.delete(`${_gongdi_mng_v10}/illegal_types/${id}`)
}


export const subcon_illegals_get=(queryParam)=>{
    let queryParamsStr =convert_query_params(queryParam)
    /* queryParam:
    {
        page integer  required:False
        per_page integer  required:False
        auditing_status integer  required:False
        subcon_name string  required:False
        illegal_typeid integer  required:False
    }*/

    return axios.get(`${_gongdi_mng_v10}/subcon_illegals${queryParamsStr}`)
}


export const subcon_illegals_post=(dataParam)=>{
    return axios.post(`${_gongdi_mng_v10}/subcon_illegals`)
}


export const subcon_illegals_id_get=(id)=>{
    return axios.get(`${_gongdi_mng_v10}/subcon_illegals/${id}`)
}


export const subcon_illegals_id_put=(id,dataParam)=>{
    return axios.put(`${_gongdi_mng_v10}/subcon_illegals/${id}`)
}


export const subcon_illegals_id_delete=(id)=>{
    return axios.delete(`${_gongdi_mng_v10}/subcon_illegals/${id}`)
}


export const subcontractors_get=(queryParam)=>{
    let queryParamsStr =convert_query_params(queryParam)
    /* queryParam:
    {
        page integer  required:False
        per_page integer  required:False
        comp_name string  required:False
        manager string  required:False
    }*/

    return axios.get(`${_gongdi_mng_v10}/subcontractors${queryParamsStr}`)
}


export const subcontractors_post=(dataParam)=>{
    return axios.post(`${_gongdi_mng_v10}/subcontractors`)
}


export const subcontractors_id_get=(id)=>{
    return axios.get(`${_gongdi_mng_v10}/subcontractors/${id}`)
}


export const subcontractors_id_put=(id,dataParam)=>{
    return axios.put(`${_gongdi_mng_v10}/subcontractors/${id}`)
}


export const subcontractors_id_delete=(id)=>{
    return axios.delete(`${_gongdi_mng_v10}/subcontractors/${id}`)
}

