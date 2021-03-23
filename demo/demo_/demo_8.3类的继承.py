# class Person(object):
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
# class Teacher(Person):
#     def __init__(self,name,gender,object):
#         # super(Teacher,self).__init__(name,gender)
#         Person.__init__(self,name,gender)
#         self.object=object
# t=Teacher('xiaoming','male','math')
# print(t.name)
# print(t.object)
# print(isinstance(t,Person))
# print(isinstance(t,object))

print('==========================================')
# class A(object):
#     def __init__(self, a):
#         print ('init A...')
#         self.a = a
#
# class B(A):
#     def __init__(self, a):
#         super(B, self).__init__(a)
#         print ('init B...')
#
# class C(A):
#     def __init__(self, a):
#         super(C, self).__init__(a)
#         print ('init C...')
#
# class D(B, C):
#     def __init__(self, a):
#         super(D, self).__init__(a)
#         print ('init D...')
# print(D.mro())
# D('d')

#============================①============================================
class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'A student who can play basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'A teacher who can play football'

class Person(object):
    pass

class Student(Person,BasketballMixin):
    pass

class Teacher(Person,FootballMixin):
    pass
s=Student()
print(s.skill())
t=Teacher()
print(t.skill())
#============================①============================================

#============================②============================================
class Person(object):
    pass
class Student(Person):
    def people(self):
        return 'A student'
class Teacher(Person):
    def people(self):
        return 'A teacher'


class SkillMixin(object):
    pass
class BasketballMixin(SkillMixin):
    def skill(self):
        return  'basketball'
class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'


class BStudent(Student, BasketballMixin):
    pass
class FTeacher(Teacher, FootballMixin):
    pass

s = BStudent()
print (s.people(),'who can play',s.skill())

t = FTeacher()
print (t.people(),'who can play',t.skill())
#============================②============================================