# 测试文件calculator_test1.py
# 创建多个测试类，一个测试类对应一种功能的测试，一种功能对应多条测试用例
import unittest

from unittest_sample.unittest_test.calculator import Calculator

# 加法测试类
class TestAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("---------class start!!--------------")
        print('\n')

    @classmethod
    def tearDownClass(cls):
        print("----------class end!!---------------")

    # 整数相加测试
    def test_add_integer(self):
        c = Calculator(6,3)
        result = c.add()
        self.assertEqual(result,9)
        print("test_add_integer finish")

    # 小数相加测试
    def test_add_decimals(self):
        c = Calculator(6.1,3.9)
        result = c.add()
        self.assertEqual(result,9)
        print("test_add_decimals finish")

    # 字符串整数相加测试
    def test_add_string(self):
        c = Calculator("6","3")
        result = c.add()
        self.assertEqual(result,9)
        print("test_add_string finish")

# 减法测试类
class TestSub(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("---------class start!!--------------")
        print('\n')

    @classmethod
    def tearDownClass(cls):
        print("----------class end!!---------------")

    # 整数相减测试
    def test_sub_integer(self):
        c = Calculator(6, 3)
        result = c.sub()
        self.assertEqual(result, 3)
        print("test_sub_integer finish")

    # 小数相减测试
    def test_sub_decimals(self):
        c = Calculator(6.9, 3.9)
        result = c.sub()
        self.assertEqual(result, 3)
        print("test_sub_decimals finish")

    # 字符串整数相减测试
    def test_sub_string(self):
        c = Calculator("6", "3")
        result = c.sub()
        self.assertEqual(result, 3)
        print("test_sub_string finish")

# 乘法测试类
class TestMul(unittest.TestCase):
    pass
# 除法测试类
class TestDiv(unittest.TestCase):
    pass


# if __name__ =='__main__':
#     # ①
#     # test_add()
#     # test_sub()
#     # test_mul()
#     # test_div()
#
#     # ②
#     # unittest.main()
#
#     # ③创建测试套件,并添加用例到套件
#     suit = unittest.TestSuite()
#     # 测试套件里添加多条用例
#     # 1）添加单条测试用例
#     # suit.addTest(TestCalculator("test_add"))
#     # suit.addTest(TestCalculator("test_sub"))
#     # suit.addTest(TestCalculator("test_mul"))
#     # suit.addTest(TestCalculator("test_div"))
#
#     # 2)添加多条用例
#     # case1 = TestCalculator("test_add")
#     # case2 = TestCalculator("test_sub")
#     # case3 = TestCalculator("test_mul")
#     # case4 = TestCalculator("test_div")
#     # suit.addTest([case1,case2,case3,case4])
#
#     # 3)添加一个测试用例类
#     # loader = unittest.TestLoader()
#     # suit.addTest(loader.loadTestsFromTestCase(TestCalculator))
#
#     # 4)添加一个模块（导入当前目录的模块？？？）
#     # loader = unittest.TestLoader()
#     # suit.addTest(loader.loadTestsFromModule(test_calculator))
#
#     # 5)添加测试用例所在的目录
#     loader = unittest.TestLoader()
#     suit.addTest(loader.discover('./test_calculator.py'))
#     # 创建测试运行器
#     # runner = unittest.TextTestRunner()
#     # runner.run(suit)