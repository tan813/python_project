import time
import unittest
from HTMLTestRunner import HTMLTestRunner

test_dir = './'

suits =unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__=='__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suits)
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = './test_report/'+now+'result.html'
    # fp = open(filename, 'w',encoding='utf-8') //用之前版本的HtmlTestRunner.py这样写
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,title='unittest_sample测试报告',description='报告如下:')
    runner.run(suits)
    fp.close()
