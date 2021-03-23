"""
fixture传参至test
fixture()param参数:可选的参数列表，它将导致多次调用fixture函数和使用它的所有测试
request 是pytest的内置 fixture ，主要用于传递参数
test_register:注册用户操作，注册之前清空用户注册表的数据
"""
import pytest


def del_sql(user):
    sql = "delete * from auth_user WHERE username = %s;" % user
    print("执行的sql:%s\n" % sql)
    # 调用执行SQL的封装函数
    # execute_sql(sql)


user = ['admin', 'root']


@pytest.fixture(scope='module', params=user)
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
    pytest.main(["-s", "test_requestParam3.py"])
