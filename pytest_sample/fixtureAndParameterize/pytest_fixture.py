"""
测试开始前的环境准备以及结束后的环境清理
①使用setup_class、teardown_class
②使用pytest.fixture装饰器
"""

from time import sleep
import pytest
from selenium import webdriver


class Test_param:

    # 类级别的Fixture
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.url = 'https://www.baidu.com'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def baidu_search(self, searchKey):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys(searchKey)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    @pytest.mark.parametrize(
        "search_key",
        ['selenium',
         'unittest',
         'parameterized'
         ],
    )
    def test_param(self, search_key):
        self.baidu_search(search_key)
        sleep(5)
        title = self.driver.title
        assert title == search_key + '_百度搜索'


if __name__ == '__main__':
    # pytest.main(['-v', './pytest_fixture.py'])
    pytest.main(['-v', '--html=./report/result.html', './pytest_fixture.py'])
