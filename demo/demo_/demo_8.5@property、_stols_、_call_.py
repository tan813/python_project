# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     @property#将get_score()装饰成属性调用
#     def s_core(self):
#         return self.score
#
#     @s_core.setter#将set_score（）装饰成属性调用
#     def s_core(self, score):
#         if score < 0 or score > 100:
#             raise ValueError('invalid score')
#         self.score = score
#
#     @property
#     def grade(self):
#         if self.score < 60:
#             return 'C'
#         if self.score < 80:
#             return 'B'
#         return 'A'
#
# s1=Student('Alice',77)
# #print(s1.get_score())
# print(s1.s_core)
# #s1.set_score(80)
# s1.s_core=80
# print(s1.s_core)
#
# s = Student('Bob', 59)
# print (s.grade)
#
# s.score = 60
# print (s.grade)
#
# s.score = 99
# print (s.grade)
#
# print('===================================================')
# class Student:
#     __slots__ = ('name','score')#限制添加属性
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
# s=Student('Bob','66')
# s.gender='Male'
# print(s.gender)
# print(s.name)

print('===================================================')
class Person:
    __slots__ = ('name','gender')
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
class Student(Person):
    __slots__ = ('score')
    def __init__(self,name,gender,score):
        super(Student, self).__init__(name,gender)
        self.score=score
s=Student('Bob','male',88)
print(s.name)
print(s.gender)
print(s.score)
print('==============================================')
class Fib(object):

    def __call__(self, num):
        a,b,L=0,1,[]
        for n in range(num):
            L.append(a)
            a,b=b,a+b
        return  L
f=Fib()
print(f(10))#输出实例用__str__,调用实例再输出用__call__
