import unittest
from time import sleep

from selenium import webdriver


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver =webdriver.Chrome()
        # self.driver.get()
        cls.base_url = "https://www.baidu.com"


    def searchBaidu(self,s_keys):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(s_keys)
        self.driver.find_element_by_id("su").click()
        sleep(2)

    def test_search_key_selenium(self):
        self.driver.get(self.base_url)
        s_keys = 'selenium'
        self.searchBaidu(s_keys)
        title = self.driver.title
        self.assertEqual(title,s_keys+"_百度搜索")

    def test_search_key_unittest(self):
        s_keys = 'unittest'
        self.searchBaidu(s_keys)
        title = self.driver.title
        self.assertEqual(title, s_keys+"_百度搜索")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()