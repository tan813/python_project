import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def findElement(self,*loc):
        return self.driver.find_element(*loc)
        # return self.driver.find_element_by_id(loc)
class BaiDu(BasePage):
    #  搜索框
    search = (By.ID,'kw')
    #  搜索框输入
    def input(self):
        self.findElement(*self.search).send_keys('selenium')
        # self.findElement('kw').send_keys('selenium')
class TestBaidu(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    bd = BaiDu(driver)
    def test_search(self):
        self.bd.input()

if __name__ == '__main__':
    unittest.main()
