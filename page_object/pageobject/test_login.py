import unittest

from selenium import webdriver

from page_object.pageobject.baidupage import BaiduPage
from page_object.pageobject.wanyipage import WanyiPage


class TestLogin(unittest.TestCase):
    '''登录网易邮箱的case'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.url = 'https://www.baidu.com'
        self.title = '百度一下'
        self.username = 'tanj3180'
        self.password = 'ymfz520..'

    # 执行用例体
    def test_login(self):
        bdpage = BaiduPage(self.driver, self.url, self.title)
        bdpage.open()  # 打开百度
        bdpage.input_login('网易邮箱登录')  # 搜索框输入网易邮箱登录
        bdpage.click_submit()  # 点击搜索
        bdpage.click_entrance()  # 点击登录入口
        # bdpage.switch_window()  # 切换句柄
        #
        wpage = WanyiPage(self.driver, self.url, self.title)
        wpage.scroll()  # 滑动到最底部
        print(self.driver.title)
        wpage.input_username(self.username)  # 输入账号
        wpage.input_password(self.password)  # 输入密码
        wpage.click_login()  # 点击登录
        assert wpage.get_name() == '谭金柏', '登录失败'  # 获取文本

    # def tearDown(self):
    #     # self.driver.quit()


if __name__ == '__main__':
    unittest.main()
