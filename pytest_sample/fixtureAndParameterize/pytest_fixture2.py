# 测试开始前的环境准备以及结束后的环境清理
# ①使用setup_class、teardown_class
# ②使用pytest.fixture装饰器
from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def init2():
    driver = webdriver.Chrome()
    yield driver
    # sleep(5)
    # driver.quit()


@pytest.mark.usefixtures('init2')
class Test_param:

    def baidu_search(self, searchKey, init2):
        driver = init2
        driver.get('https://www.baidu.com')
        driver.find_element_by_id('kw').send_keys(searchKey)
        driver.find_element_by_id('su').click()
        sleep(2)

    @pytest.mark.parametrize(
        "search_key",
        ['selenium',
         'unittest',
         'parameterized'
         ],
        # ids=['case1', 'case2', 'case3']
    )
    def test_param(self, search_key, init2):
        driver = init2
        self.baidu_search(search_key, init2)
        sleep(1)
        title = driver.title
        assert title == search_key + '_百度搜索'
        print('finished!')


if __name__ == '__main__':
    pytest.main(['-s', '--html=./report/test.html', 'pytest_fixture2.py'])
