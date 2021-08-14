"""
用例执行失败，测试报告生成截图
调用 conftest.py
"""
import time
from time import sleep
import pytest


class Test_param:



    def baidu_search(self, searchKey, browser):
        browser.get('https://www.baidu.com')
        browser.maximize_window()
        browser.find_element_by_id('kw').send_keys(searchKey)
        browser.find_element_by_id('su').click()
        sleep(1)

    @pytest.mark.parametrize(
        "search_key",
        ['selenium',
         # 'unittest',
         # 'parameterized'
         ],
    )
    def test_param(self, search_key, browser):
        """测试pytest参数化搜索"""
        self.baidu_search(search_key, browser)
        title = browser.title
        # pytest.xfail("功能尚未完成!!!")
        assert title == search_key + '_1百度搜索'


if __name__ == '__main__':
    now = time.strftime("%H_%M_%S")
    pytest.main(['-s','-v', '--html=./report/'+now + 'result.html', './test_baidu_search.py'])