"""
用例b、c的执行依赖于用例a，用例a失败直接给b、c标记xfail，跳过执行
"""
import pytest

data = [{"user": "admin", "psw": ""}]


@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    psw = request.param["psw"]
    print("正在操作登录，账号：%s，密码：%s" % (user, psw))
    if psw:
        return True
    else:
        return False


@pytest.mark.parametrize("login", data, indirect=True)
class Test_x_fail:

    def test_a(self, login):
        """用例a登录"""
        result = login
        assert result

    def test_b(self, login):
        """用例b"""
        result = login
        if not result:
            pytest.xfail("登录用例执行失败，跳过执行")
        assert 1 == 1

    def test_c(self, login):
        """用例c"""
        result = login
        if not result:
            pytest.xfail("登录用例执行失败，跳过执行")
        assert 2 == 2


if __name__ == "__main__":
    pytest.main(['-s', 'test_xfail.py'])
