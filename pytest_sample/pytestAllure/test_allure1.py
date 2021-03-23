# coding=gbk
"""
生成allAure测试报告
"""
import os

from time import sleep

import allure
import pytest


class TestAllure:

    def test_allure_py19(self, browser):
        with allure.step("step1：打开百度首页"):
            browser.get("https://www.baidu.com/")
        with allure.step("step2：输入搜索关键字"):
            browser.find_element_by_id("kw").send_keys("allurePytest22")
        with allure.step("step3：点击搜索"):
            browser.find_element_by_id("su").click()
            sleep(1)
        # 故断言失败，看是否会截图
        assert browser.title == "allure_百度搜索"


if __name__ == '__main__':
    # 执行用例，生成 Allure 报告需要的数据存在allure-datas目录
    # 若没有allure-datas目录会自动创建,并不是说可以不要这个参数
    # --clean-alluredir参数清allure-datas目录下的数据文件(两种写法),
    pytest.main(['test_allure1.py', '--alluredir=allure-datas', '--clean-alluredir'])
    # os.system('pytest test_allure1.py --alluredir=allure-results --clean-alluredir')

    # 执行命令 allure generate ，生成测试报告,
    # 报告默认生成在allure-report目录(没有该目录则自动生成)
    # -c参数清上次运行的报告记录
    os.system('allure generate -c allure-datas')
    # 指定报告生成目录allure_report,需要添加-o参数(输出文件)
    # os.system('allure generate -c allure-datas -o allure_report')

    # 打开报告
    # os.system('allure open allure-report')
