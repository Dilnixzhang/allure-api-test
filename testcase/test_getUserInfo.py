import pytest
import requests
from common.commonData import CommonData
from conftest import http

class Test_getUserinfo:
    def test_getUserInfo(self):
        path = '/sys/getUserInfo'
        data = {'token': CommonData.token}
        resp_getUserInfo = http.post(path, data)
        return resp_getUserInfo

