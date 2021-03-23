import unittest
import codecs
import csv
from itertools import islice
from time import sleep

from selenium import webdriver


class testBaidu(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = 'https://www.baidu.com'
        # 读取本地csv文件
        cls.datas = csv.reader(codecs.open('./test.csv', 'r', 'gb2312'))
        # 存放读取数据
        cls.case = []
        for data in islice(cls.datas, 1, None):
            cls.case.append(data)

    def baidu_search(self, key):
        self.driver.get(self.url)
        self.driver.find_element_by_id('kw').send_keys(key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    def test_case1(self):
        self.baidu_search(self.case[0][1])
        title = self.driver.title
        self.assertEqual(title, self.case[0][1] + "_百度搜索")

    def test_case2(self):
        self.baidu_search(self.case[1][1])
        title = self.driver.title
        self.assertEqual(title, self.case[1][1] + "_百度搜索")

    def test_case3(self):
        self.baidu_search(self.case[2][1])
        title = self.driver.title
        self.assertEqual(title, self.case[2][1] + "_百度搜索")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)