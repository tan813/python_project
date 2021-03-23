import unittest

from TestRunner import HTMLTestRunner

test_dir = '.'
suits =unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__=='__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suits)
    fp = open('./test_report/result.html', 'w',encoding='utf-8')
    runner = HTMLTestRunner(stream=fp,title='unittest_sample测试报告',description='报告如下:')
    runner.run(suits)
    fp.close()
