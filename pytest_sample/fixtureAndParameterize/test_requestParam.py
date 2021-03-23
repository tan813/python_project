# coding=gbk
"""
indirect = true
登录操作放到前置操作里，test传参至fixture
request 是pytest的内置 fixture ，主要用于传递参数
用request.param接收
"""
import pytest

# 测试数据
test_data = [
    {"user": "admin", "pwd": "123"},
    {"user": "admin1", "pwd": "1234"},
]


@pytest.fixture(scope="module")
def login(request):
    # request.param 接收的是一个字典
    user = request.param['user']
    pwd = request.param['pwd']

    print("\n登录账户：%s,\n登录密码：%s" % (user, pwd))

    """
    获取到账号密码执行登录
    execute_login(user,pwd)
    """
    if pwd:
        return True
    else:
        return False


# indirect = True,login以函数的形式执行，test_data里的数据作为参数往login()传
@pytest.mark.parametrize("login", test_data, indirect=True)
def test_login(login):
    a = login
    print(a)


if __name__ == "__main__":
    pytest.main(["-s", "test_requestParam.py"])
