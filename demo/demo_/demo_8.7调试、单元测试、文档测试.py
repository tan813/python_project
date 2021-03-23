# #①使用print把可能有问题的变量打印出来
#
# #②使用assert断言
s='0'
n=int (s)
assert n!=0,'分母不能为0'
print(10/n)
#③使用logging，有debug，info，warning，error等几个级别，当我们指定level=WARNING时，logging.info
#就不起作用了,后同理
import logging
logging.basicConfig(level=logging.WARNING)
s='0'
n=int(s)
logging.info('n=%d'%n)
logging.warning('n is zero')
print(10/n)
#④pdb  D:\Users\lenovo\Python_project\demo>python -m pdb demo_\demo_***.py

s = '0'
n = int(s)
print(10 / n)

#⑤ pdb.set_trace
import pdb
s='0'
n=int(s)
pdb.set_trace()
print(10/n)
print('========================================================')
from unittest_sample import unittest_test


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score<0 or self.score>100:
            raise ValueError
        if self.score >= 60 and self.score<80:
            return 'B'
        if self.score >= 80 :
            return 'A'
        else:
            return 'C'

#单元测试的意义：在修改的时候，可以极大程度地保证该模块行为仍然是正确的。
#如果通过，说明我们的修改不会对get_grade()函数原有的行为造成影响，
# 如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。
class TestStudent(unittest_test.TestCase):
    def setUp(self):
        print('setUp...')

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

    def tearDown(self):
        print('tearDown...')

if __name__ == '__main__':
    unittest_test.main()
print('===========================================================')
class Dict(dict):
  # def __init__(self,age,name):
  #     self.name=name
  #     self.age=age
  def __init__(self,**kw):
      super(Dict, self).__init__(**kw)
  def __getattr__(self, key):
      return self[key]
d=Dict(name='bob',age=11)
print(d.age)


print('===========================================================')

def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()