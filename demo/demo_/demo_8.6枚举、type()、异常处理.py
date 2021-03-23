from enum import Enum, unique



class Month(Enum):
    Jan,Feb=1,2
    Mar=3
    Apr=4
    May=5
    Jun=6
    Jul=7
    Aug=8
    Sep=9
    Oct=10
    Nov=11
    Dec=12
print(Month['Jan'])#通过成员名获取成员

print(Month(1))#通过成员值获取成员

print(Month.Jan.name)#成员的名称

print(Month.Jan.value)#成员的值

for member in Month:
    print(member)

for member in Month.__members__.items():
 print(member)
# print('===========================================================')
@unique
class Gender(Enum):
    Male=0
    Female=1
class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
Bob=Student('Bob',Gender.Female)
print(Bob.name)
print(Bob.gender.value)

print(type(123))
print(type(Student))
print(type(Bob))
from functools import reduce

print('===========================================================')
#使用type来创建类，type（)既可以返回对象的类型，也可以创建出新的类型
def fn(self,name):
    print('hello, %s '%name)
Hello=type('Hello',(object,),dict(hello=fn,age=6))
#其中字典的 key 就是类变量或方法名，如果字典的 value 是普通值，那就代表类变量；
# 如果字典的 value 是函数，则代表方法
h=Hello()
print(h.hello('world'))
print(Hello.age)


print('===========================================================')
# class IntError(ValueError):
#     pass
# def str2num(s):
#     if '.' in s:
#         raise IntError('invalid value:%s'%s)
#     return int(s)
def str2num(s):
    try:
     return int(s)
    except ValueError as e:
        print('except:',e)
        return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)

main()

print('==================================')
import logging
def div(x,y):
    return x/y
def main():
    try:
     d=div(4,0)
    except Exception as e:
        logging.exception(e)
    else:
     print(d)
main()