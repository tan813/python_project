# -*- coding: utf-8 -*-
"""
@Author   : tanjinbai
@Time     : 2021-08-08 21:43
@Function : pytest执行登录用例
"""
import pytest
import yaml

from page_object.poMode.keywords import SimWeb

with open('test_case.yaml', 'r', encoding='utf-8') as yamlFile:
    cases_dit = yaml.safe_load(yamlFile)


class Test_SimWeb:

    def run_step(self, func, value):
        func(*value)

    def setup_class(self):
        self.web = SimWeb()
        self.web.open_browser()

    @pytest.mark.parametrize('poCases', cases_dit['loginPage'])
    def test_login(self, poCases):
        cases = poCases['cases']
        try:
            for case in cases:
                func = self.web.__getattribute__(case['method'])
                """
                __getattribute__方法获取web对象的属性，当类中属性被访问,
                会自动调用与该属性同名的方法,返回的是该方法的引用
                传字符串过去即可使用该方法
                上述过程称之为"反射"
                """
                caselist = list(case.values())
                self.run_step(func, caselist[2:])
                self.web.sleep()
        except:
            raise

    def teardown_class(self):
        self.web.quit()
