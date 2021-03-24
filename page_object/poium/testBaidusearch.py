import unittest

from selenium import webdriver

from project_example.example1.page import BaiduPage


class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_baidusearch(self):
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com/")
        page.search_input = "poium"
        page.search_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
