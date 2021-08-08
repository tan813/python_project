# -*- coding: utf-8 -*-
"""
@Author   : tanjinbai
@Time     : 2021-08-08 20:05
@Function : yaml与python数据类型的转换
"""
import yaml

with open("test_case.yaml", "r", encoding="utf-8") as yamlFile:
    cases_dict = yaml.safe_load(yamlFile)  # {loginPage:[]}
    # print(case_dict)

    cases_list = cases_dict['loginPage']   # [{'title':'', 'case':'[]'}]
    # print(cases_list)

    cases = cases_list[0]['cases']         # [{'step':''}, {'step':''}]
    # print(cases)

    for case in cases:
        value_list = list(case.values())
        print("当前调用的方法是：" + case['method'])
        print(value_list)


"""
{loginPage': [
              {'title': '登录成功',  'desc': '登录的用例',
               'cases': [{'step': '打开登录页', 'method': 'geturl', 'url': 'http:www.baidu.com'},
                         {'step': '输入账号', 'method': 'input', 'locator': '#kw', 'value': '15197230072'},
                         {'step': '输入密码', 'method': 'input', 'locator': '.pw', 'value': '123456'},
                         {'step': '点击登录', 'method': 'click', 'locator': '#cl'}
                        ]
              }
             ]
}
"""
