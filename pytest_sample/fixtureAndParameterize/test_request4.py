# -*- coding: utf-8 -*-
"""
@Author   : tanjinbai
@Time     : 2021-08-22 10:15
@Function : 登录操作放到前置操作，使用pytest.mark.parametrize传参至fixture，不同账号执行不同用例
"""
import pytest

userDate1 = [{'acc': 'admin', 'pwd': '12345'}]
userDate2 = [{'acc': 'root', 'pwd': '12345'}]


@pytest.fixture()
def login(request):
    account = request.param['acc']
    password = request.param['pwd']
    """
    execute_login(account,password)
    """
    print("当前登录的账号是%s!" % account)


@pytest.mark.parametrize('login', userDate1, indirect=True)
def test_case1(login):
    pass
    print("执行用例1!")


@pytest.mark.parametrize('login', userDate2, indirect=True)
def test_case2(login):
    pass
    print("执行用例2!")


if __name__ == '__main__':
    pytest.main(['-s', 'test_request4.py'])
