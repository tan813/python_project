"""
fixture 与reruns一起使用
"""
from time import sleep

import pytest


def test_s1(browser):
    print("\nbrowser is %s" % browser)
    browser.get('https://www.baidu.com/')
    browser.find_element_by_id('kw').send_keys('reruns')
    browser.find_element_by_id('su').click()
    sleep(2)
    assert browser.title == 'reruns_百度搜索！'


# def test_s2(browser):
#     test_s1(browser)
#     browser.find_element_by_id('su').click()
#     sleep(2)
#     assert 0


if __name__ == '__main__':
    pytest.main(['-s', '-v', '--reruns', '1', 'test_fixtureReruns.py'])
