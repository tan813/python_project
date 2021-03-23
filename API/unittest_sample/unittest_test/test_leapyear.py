# 测试文件
import unittest
from unittest_sample.unittest_test.leapyear import LeapYear


class TestLeapYear(unittest.TestCase):
    def test_2000(self):
        ly = LeapYear(2000)
        self.assertEqual(ly.answer(),"2000是闰年")

    def test_2004(self):
        ly = LeapYear(2004)
        self.assertEqual(ly.answer(),"2004是闰年")

    def test_2007(self):
        ly = LeapYear(2007)
        self.assertEqual(ly.answer(),"2007不是闰年")

# if __name__=="__main__":
#     unittest.main()