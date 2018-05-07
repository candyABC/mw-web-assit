import pytest
from src.mw_web_assit.gen_api import ApiMethods

def test_gen_api():
    api =ApiMethods()
    api.parse('./files/gongdi_mng.yaml','./files/gongdi_mng.js')

test_gen_api()