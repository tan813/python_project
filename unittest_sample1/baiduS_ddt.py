import unittest
from time import sleep

from ddt import ddt, data, unpack, file_data
from selenium import webdriver

@ddt
class testBaidu(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = 'https://www.baidu.com'

    def baidu_search(self, searchKey):
        self.driver.get(self.url)
        self.driver.find_element_by_id('kw').send_keys(searchKey)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    # @data(['case1','selenium'],['case2','unittest'],['case3','parameterized'])
    # @unpack
    #def test_case(self, name, searchKey):

    #参数化读取json文件
    @file_data('data.json')
    def test_case(self,searchKey):
        self.baidu_search(searchKey)
        title = self.driver.title
        self.assertEqual(title, searchKey + "_百度搜索")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)