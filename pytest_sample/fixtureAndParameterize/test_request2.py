"""
多个前置操作支持parametrize装饰器叠加
"""
import pytest

# test_datas = [
#     {"user": "admin", "pwd": "1234"},
#     {"user": "admin1", "pwd": "12345"}
# ]
user_datas = ("admin", "admin1")
pwd_datas = ("1234", "12345")


@pytest.fixture(scope="module")
def input_user(request):
    user = request.param
    return user


@pytest.fixture(scope="module")
def input_pwd(request):
    pwd = request.param
    return pwd


# 传的数据是一个字符串，把"admin"和"1234"一个字母一个字母往input_user()、input_pwd()传,
# @pytest.mark.parametrize("input_user", test_datas[0]["user"], indirect=True)
# @pytest.mark.parametrize("input_pwd", test_datas[0]["pwd"], indirect=True)

# 传的数据是一个元组，把元组的元素"admin"和"admin1"往input_user()传
@pytest.mark.parametrize("input_user", user_datas, indirect=True)
# 传的数据是一个元组，把元组的元素"admin"和"admin1"往input_pwd()传
@pytest.mark.parametrize("input_pwd", pwd_datas, indirect=True)
def test_login(input_user, input_pwd):
    a = input_user
    b = input_pwd
    print("测试数据:user -> %s , password ->%s" % (a, b))


if __name__ == "__main__":
    pytest.main(['-s', 'test_request2.py'])
