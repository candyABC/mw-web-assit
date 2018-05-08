import pytest
from src.mw_web_assit.swagger_helper import SwaggerHelper

def test_gen_api():

    helper =SwaggerHelper('./files/gongdi_mng.yaml')
    helper.gen('./files/','gongdi')

test_gen_api()