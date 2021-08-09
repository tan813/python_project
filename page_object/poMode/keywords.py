# -*- coding: utf-8 -*-
"""
@Author   : tanjinbai
@Time     : 2021-08-08 21:14
@Function : 创建SimWeb类定义关键字方法!
"""
from time import sleep

from selenium import webdriver


class SimWeb:
    def __int__(self):
        self.br = 'gc'
        self.driver: webdriver.Chrome()

    def open_browser(self, browser='gc'):
        if browser == 'gc' or browser == '':
            self.br = 'gc'
            self.driver = webdriver.Chrome()
        elif browser == 'ff':
            self.br = 'ff'
            self.driver = webdriver.Firefox()
        else:
            self.br = 'gc'
            print('不支持的浏览器类型，默认使用google chrome')

    def __find_element(self, locator=''):
        if locator is None or locator == '':
            return None
        elif locator.startswith('/'):
            return self.driver.find_element_by_xpath(locator)
        elif locator.startswith('#') or locator.__contains__('>'):
            return self.driver.find_element_by_css_selector(locator)
        else:
            return self.driver.find_element_by_id(locator)

    def click(self, locator):
        ele = self.__find_element(locator)
        ele.click()

    def input(self, locator, value):
        ele = self.__find_element(locator)
        ele.send_keys(value)

    def geturl(self, url):
        self.driver.get(url)

    def sleep(self, t=2):
        sleep(t)

    def quit(self):
        self.driver.quit()
