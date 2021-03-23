# 测试文件calculator_test.py
import unittest

import pytest

from unittest_sample.unittest_test.calculator import Calculator


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n')
        print("------class start!--------")
        # print('\n')

    @classmethod
    def tearDownClass(cls):
        print("-------class end!---------")

    # def setUp(self):
    #     print("test start!")
    #
    # def tearDown(self):
    #     print("test end!")

    def test_add(self):
        c = Calculator(6,3)
        result = c.add()
        # assert result==9,'加法运算失败!'
        # TestCalculator().assertEqual(result,9)
        self.assertEqual(result,9)
        print('test_add finished!')


    def test_sub(self):
        c = Calculator(6,3)
        result = c.sub()
        # assert result==3,'减法运算失败!'
        TestCalculator().assertEqual(result, 3)
        print('test_sub finished!')

    @pytest.mark.doo
    def test_mul(self):
        c = Calculator(2,3)
        result = c.mul()
        # assert result==6,'乘法运算失败！'
        TestCalculator().assertEqual(result, 8)
        print('test_mul finished!')

    def test_div(self):
        c = Calculator(6,2)
        result = c. div()
        #assert result==3,'除法运算失败!'
        TestCalculator().assertEqual(result, 3)
        print('test_div finished!')


# if __name__ =='__main__':
# #
# #
# #         # 创建测试套件,并添加用例到套件
# #         suit = unittest.TestSuite()
# #
# #         # 4)添加一个模块（导入当前目录的模块？？？）
# #         loader = unittest.TestLoader()
# #         suit.addTest(loader.loadTestsFromModule(test_calculator))
# #
# #         #创建测试运行器
# #         runner = unittest.TextTestRunner()
# #         runner.run(suit)