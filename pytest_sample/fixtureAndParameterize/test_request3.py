"""
fixture传参至test
fixture()param参数:可选的参数列表，它将导致多次调用fixture函数和使用它的所有测试
request 是pytest的内置 fixture ，主要用于传递参数
"""
import pytest


def del_sql(use):
    sql = "delete * from auth_user WHERE username = %s;" % use
    print("执行的sql:%s\n" % sql)
    # 调用执行SQL的封装函数
    # execute_sql(sql)


user_data = ['admin', 'root']


@pytest.fixture(scope='module', params=user_data)
def user(request):
    # 前置操作:清空注册表数据
    del_sql(request.param)

    yield request.param

    # 后置操作:...


def test_register(user):
    # 执行注册操作
    # ...
    print("%s 注册成功!!!\n" % user)


if __name__ == "__main__":
    pytest.main(["-s", "test_request3.py"])
