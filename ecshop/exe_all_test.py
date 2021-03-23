import unittest
from HTMLTestRunner import HTMLTestRunner

from ecshop.demo.send import send_mail

import time
# from HTMLTestRunner import HTMLTestRunner


test_report = "D:\\Users\\lenovo\\Python_project\\ecshop\\testresult"
# 使用unittest默认的测试用例加载器，加载所有的用例
dis= unittest.defaultTestLoader.discover("D:\\Users\\lenovo\\Python_project\\ecshop\\testcase", "*")
#新建并打开一个报告文件
now = time.strftime("%Y-%m-%d_%H_%M_%S")
filename = test_report + '\\'+now + '_result.html'
file = open(filename,"wb")
#新建一个报告
htr=HTMLTestRunner(stream=file,title="ECSHOP自动化测试报告",description="报告如下:")
#通过报告去运行所有的用例
htr.run(dis)
file.close()#不加，当测试全部通过获取不到html文件内容

# lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
# lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
# file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new

se=send_mail(filename)
se.enclosuremail()


