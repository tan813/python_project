import unittest

from selenium import webdriver

from page_object.poium.baidupage import BaiduPage


class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_baidu_search(self):
        # 传浏览器驱动是因为PageObject类中有初始化driver的操作
        page = BaiduPage(self.driver)
        # 调用的是PageObject类中的get方法，BaiduPage继承Page，Page继承PageObject
        page.get("https://www.baidu.com/")
        page.search_input = "poium"
        page.search_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
