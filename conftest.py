import pytest
import requests
from common.commonData import CommonData
from util.httpUtil import HttpUtil

http = HttpUtil()

@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    path = '/sys/login'
    data = {"userName":"18210034706","password":"123456"}
    resp_login = http.post(path,data)
    CommonData.token = resp_login['object']['token']
    # assert resp_login.status_code == 200



















#第一天：
# http = requests.session()
# @pytest.fixture(scope='session',autouse=True)
# def session_fixture():
#     proxies = {'http': 'http://localhost:8888'}
#     headers = {'Content-Type': 'application/json;charset=UTF-8'}
#     print(headers)
#     resp_login = http.post(url="http://192.168.1.203:8083/sys/login",
#                      proxies=proxies,
#                      data='{"userName":"18210034706","password":"123456"}',
#                      headers=headers)
#     resp_dict = json.loads(resp_login.text)
#     token = resp_dict['object']['token']
#     assert resp_login.status_code == 200
#     print("login")
#     yield
#     headers['token'] = token
#     resp_logout = http.post(url="http://192.168.1.203:8083/sys/logout",
#                      proxies=proxies,
#                      data=None,
#                      headers=headers)
#     assert resp_logout.status_code == 200
#     print("logout")
