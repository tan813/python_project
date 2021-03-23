# allure装饰器方法：
# @allure.step()\with allure.step()添加测试用例步骤
# allure.attach(content,name,type)添加附件，content附件的内容，name附件名称，type附件类型（allure.attachment_type其中一种）
# allure.attach.file(source,name,type)添加附件文件，source文件路径
# @allure.epic()添加总体描述                                  Eg:@allure.epic("项目名称")
# @allure.feature()添加功能模块描述，多用于修饰Class类        Eg:@allure.feature("登录模块")
# @allure.story()添加用例模块描述，多用于修饰testcase方法     Eg:@allure.story("账号xxx，密码xxx，登录成功/失败")
# @allure.title()修改allure报告中用例的标题，默认标题为测试用例函数名函数名,相当于具体每条用例的描述
# @allure.description()添加测试用例描述，与''' xxx '''一样的效果
# @allure.link(url,name)添加跳转链接，与issue()、testcase()类似，样式不一样


import os

import allure
import pytest


@allure.epic("JJ Shop Project")
@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    @allure.title("账号密码均正确，登录成功。")
    @allure.description("账号:123456，密码:zxc均正确，登录成功。")
    def test_login_success(self, browser):
        with allure.step("1、打开项目网址"):
            browser.get("https://www.baidu.com/")
        with allure.step("2、输入账号"):
            enter_account('123456')
        with allure.step("3、输入密码"):
            enter_password('zxc')
        with allure.step("4、点击登录"):
            click_login()

        # 断言预期结果与实际结果相同（Eg:title是登录后的title）
        assert 1 == 1

    @allure.story("登录失败")
    @allure.title("账号正确密码错误，登录失败。")
    @allure.description("账号:123456，密码:zxx错误，登录失败。")
    def test_login_failure(self):
        with allure.step("1、输入账号"):
            enter_account('123456')
        with allure.step("3、输入密码"):
            enter_password('zxx')
        with allure.step("4、点击登录"):
            click_login()
        # 断言预期结果与实际结果相同（Eg:title是登录前的title）
        assert 1 == 1

    @allure.story("登录失败")
    @allure.title("账号错误密码正确，登录失败。")
    @allure.description("账号:12345，密码:zxc正确，登录失败。")
    def test_login_failure1(self):
        with allure.step("1、输入账号"):
            enter_account('12345')
        with allure.step("3、输入密码"):
            enter_password('zxc')
        with allure.step("4、点击登录"):
            click_login()
        # 断言预期结果与实际结果相同（Eg:title是登录前的title）
        assert 1 == 2


@allure.feature("购物车模块")
class TestShopCar:
    @allure.story("浏览商品")
    @allure.title("点击商品图标，商品信息能正常显示")
    @allure.description("点击商品图标，商品图片、价格、详细信息正常显示。")
    def test_browse_goods(self):
        with allure.step("1、点击商品图标"):
            pass
        with allure.step("2、点击查看详情"):
            pass
        allure.attach.file('./shoes.jpg', '老北京布鞋', attachment_type=allure.attachment_type.JPG)
        # 断言预期结果与实际结果相同（Eg:title是详情页的title）
        assert 1

    @allure.story("添加购物车")
    @allure.title("点击添加按钮，能成功加入购物车")
    @allure.description("点击添加按钮，成功加入购物车，提示加入购物车成功。")
    @allure.link('https://www.tapd.cn/', name='bug issue链接')
    # 此条模拟为bug用例
    def test_add_car(self):
        with allure.step("点击添加按钮加入购物车"):
            pass
        # 断言提示信息为"加入购物车成功",但实际不是
        assert 0


def enter_account(account_number):
    print('账号:' + account_number)


def enter_password(password):
    print('密码:' + password)


def click_login():
    pass


if __name__ == '__main__':
    pytest.main(
        ['test_allureFunc.py', '--alluredir=allure-datas', '--clean-alluredir'])
    os.system('allure generate -c allure-datas')
