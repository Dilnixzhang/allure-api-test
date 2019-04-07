import pytest
import requests
import json
from util.httpUtil import HttpUtil
from common.commonData import CommonData
from conftest import http
class Test_login:
    def test_login(self):
        path = '/sys/login'
        data = {"userName": CommonData.userName, "password": CommonData.password}
        # data['userName'] = '18210034706'
        # data['password'] = '123456'
        resp_login = http.post(path, data)
        assert resp_login['code'] == 200
        assert resp_login['msg'] == '操作成功'
        assert resp_login['object']['userId'] == 165
        # CommonData.token = resp_login['object']['token']

    def test_login_pwd_fail(self):
        path = '/sys/login'
        data = {"userName": CommonData.userName, "password": "1234756"}
        resp_login_pwd_fail=http.post(path,data)
        assert resp_login_pwd_fail['code'] == 410
        assert resp_login_pwd_fail['msg'] == '用户名或密码错误'

    def test_login_user_fail(self):
        path = '/sys/login'
        data = {"userName": "18723456709", "password": "1234756"}
        resp_login_user_fail = http.post(path, data)
        assert resp_login_user_fail['code'] == 301
        assert resp_login_user_fail['msg'] == '用户不存在'


