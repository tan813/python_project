# #isinstance、type、dir获取变量类型/实例属性
# from functools import cmp_to_key
#
#
# class Person(object):
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
# class Student(Person):
#     def __str__(self):
#         return '(Student:%s,%s,%s)'%(self.name,self.gender,self.score)
#
#     def __init__(self,name,gender,score):
#         super(Student, self).__init__(name,gender)
#         self.score=score
#     def whoAmI(self):
#         return 'I am a student'
#
# s=Student('Alice','Male','77')
# print(type(s))
# print(list(filter(lambda x:x[0]!='_',dir(s))))
# print(s)
#
# print('===========================================================')
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def __str__(self):
#         return '(%s: %s)' % (self.name, self.score)
#
#     __repr__ = __str__
#
# def f_cmp(x, s):
#         if x.score<s.score:
#             return 1
#         elif x.score>s.score:
#             return -1
#         else:
#             if x.name<s.name:
#                 return -1
#             return 1
# L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
# print(sorted(L,key=cmp_to_key(f_cmp)))
# print('===========================================================')
# class Students(object):
#     def __init__(self, *args):
#          self.names = args
#     def __len__(self):
#         return len(self.names)
# s=Students('aaa','bb','ccc')
# print(len(s))
print('===========================================================')
class Fib(object):
    def __init__(self,num):
      a,b,L=0,1,[]
      for i in range(num):
        L.append(a)
        a,b=b,a+b#同时更新，不能分开，a未更新之前得值+b赋值给b
        # a=b
        # b=a+b
        self.fib=L#直接使用L则只能在该方法内使用,或者适用self.L
    def __str__(self):
        return str(self.fib)
    def __len__(self):
        return len(self.fib)

f=Fib(10)
print(f)
print(len(f))

print('===========================================================')
#斐波那契数列创建
fbi=[0,1]
for i in range(8):
    fbi.append(fbi[-1]+fbi[-2])
print(fbi)

print('===========================================================')



class Rational(object):
    def gcd(self,a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.p,self.q * r.q)
    def __truediv__(self, r):
        return Rational(self.p * r.q, self.q * r.p)
    def __str__(self):
        g=self.gcd(self.p,self.q)
        return '%s/%s' % (self.p//g, self.q//g)
f1=Rational(2,5)
f2=Rational(10,6)
print(f1/f2)

print('===========================================================')
class Rational(object):
    def __init__(self,p,q):
        self.p=p
        self.q=q
    def __int__(self):
        return self.p//self.q
    def __float__(self):
        return self.p/self.q
print(int(Rational(3,2)))
print(float(Rational(4,2)))
