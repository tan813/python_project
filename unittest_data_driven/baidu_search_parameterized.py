import unittest
from time import sleep

from parameterized import parameterized
from selenium import webdriver


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = 'https://www.baidu.com'

    def baidu_search(self, caseNum, searchKey):
        self.driver.get(self.url)
        self.driver.find_element_by_id('kw').send_keys(caseNum+searchKey)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    @parameterized.expand([
        ('case1', 'selenium'),
        ('case2', 'unittest'),
        ('case3', 'parameterized')
        # 'selenium',
        # 'unittest',
        # 'parameterized'
    ])
    def test_case(self, caseNum, searchKey):
        self.baidu_search(caseNum, searchKey)
        title = self.driver.title
        self.assertEqual(title, caseNum+searchKey + "_百度搜索")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
