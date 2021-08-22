# -*- coding: utf-8 -*-
"""
@Author   : tanjinbai
@Time     : 2021-08-22 10:58
@Function : 使用同一账号执行不同用例可使用@pytest.fixture()中params参数直接进行传参
            不同账号执行不同用例用params参数实现需再写个fixture函数login1()，
            不如用pytest.mark.parametrize()实现简便
"""
import pytest

# 这样传每个用例跑2遍，用admin、root各一次
# userDate1 = [{'acc': 'admin', 'pwd': '12345'}, {'acc': 'root', 'pwd': '12345'}]
userDate1 = [{'acc': 'admin', 'pwd': '12345'}]


@pytest.fixture(params=userDate1)
def login(request):
    account = request.param['acc']
    password = request.param['pwd']
    """
    execute_login(account,password)
    """
    print("当前登录的账号是%s!" % account)


# @pytest.mark.parametrize('login', userDate1, indirect=True)
# def test_case1(login):
#     pass
#     print("执行用例1!")
def test_case1(login):
    pass
    print("执行用例1!")


# @pytest.mark.parametrize('login', userDate2, indirect=True)
# def test_case2(login):
#     pass
#     print("执行用例2!")
def test_case2(login):
    pass
    print("执行用例2!")


if __name__ == '__main__':
    pytest.main(['-s', 'test_request5.py'])
