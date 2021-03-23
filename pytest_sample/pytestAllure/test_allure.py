import os
import time
from time import sleep

import allure
import pytest


def test_allure_py12(browser):
    with allure.step("step1：打开百度首页"):
        browser.get("https://www.baidu.com/")
    with allure.step("step2：输入搜索关键字"):
        browser.find_element_by_id("kw").send_keys("allurePytest")
    with allure.step("step3：点击搜索"):
        browser.find_element_by_id("su").click()
        sleep(1)
    # 故断言失败，看是否会截图
    assert browser.title == "allure_12345百度搜索"


if __name__ == '__main__':
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在report目录
    # 若没有report目录会自动创建
    pytest.main(['./test_allure.py', '--alluredir', './report'])

    # 执行命令 allure generate ，生成测试报告
    # 其中report是之前装allure文件的目录,clean是清除原先文件夹里的报告
    # 报告生成默认存在allure-report目录(没有该目录则自动生成)
    os.system('allure generate ./report --clean')

    # 指定报告生成目录allure_report,需要添加-o参数指明是输出文件
    # os.system('allure generate ./report -o ./allure_report --clean')
