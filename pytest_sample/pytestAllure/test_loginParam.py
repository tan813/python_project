# 测试不同数据
# 每组数据不同结果，不同title
# 参数化动态生成标题
import os

import allure
import pytest


def login(username, password):
    print("输入账号:%s" % username)
    print("输入密码:%s" % password)
    return {"code": 0, "msg": "success"}


test_datas = [
    ({"username": "tan", "password": "123"}, 'success', "输入正确账号，密码，登录成功"),  # 每一组数据的title描述
    ({"username": "tan1", "password": "123"}, 'success', "输入正确账号，密码，登录成功"),
    ({"username": "tan", "password": "1234"}, 'failed', "输入错误账号，密码，登录失败"),
]


# allure.title传入参数
@allure.title("登录测试用例-{title}")
@pytest.mark.parametrize(
    'test_input,expected,title',
    test_datas,
)
def test_login(test_input, expected, title):
    result = login(test_input['username'], test_input['password'])
    assert result['msg'] == expected


if __name__ == '__main__':
    pytest.main(['test_loginParam.py', '--alluredir=allure-datas', '--clean-alluredir'])
    os.system('allure generate -c allure-datas')
