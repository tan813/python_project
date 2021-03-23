#关键字参数

def shop (where='store',what='pen'):
    print('I want you to go to the',where,'and buy a',what)
shop()

print('========================================')

def shop(**kw):
    for k,v in kw.items():
        print(k,v)
shop(a=9,b=12,c=21)

print('========================================')
class Person:
    def __init__(self,name,gender,bir,**kw):
        self.name=name
        self.gender=gender
        self.bir=bir
        for k,v in kw.items():
           setattr(self,k,v)
            # self.k=v # 设置属性k的值为v，不是kw里面的k

xiaoming=Person('xiaoming','male','1990-1-1',age=18,job='student')
print(xiaoming.age)
print(xiaoming.job)

print('========================================')
class Person:
    def __init__(self,score):
        self.__score=score
    def get_grade(self):
        if self.__score>=90:
            print('A-优秀')
        elif self.__score>=60 and self.__score<90:
            print('B-及格')
        else:
            print ('C-不及格')

p1=Person(76)
p1.get_grade()

print('========================================================')
class Person:
    count=0#类的属性count
    def __init__(self,name):#每创建实例都要调用__init__方法
       self.name=name
       Person.count=Person.count+1

p1=Person('lihua')
p2=Person('xiaoming')
p3=Person('xiaojun')
print(Person.count)

print('========================================================')
class Person:
    __count=0#私有属性
    @classmethod
    def cal_count(cls):
        return cls.__count
    def __init__(self,name):#每创建实例都要调用__init__方法
       self.name=name
       Person.__count=Person.__count+1

p1=Person('lihua')
p2=Person('xiaoming')
p3=Person('xiaojun')
print(Person.cal_count())

print('======================================================')


class exp(object):

    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    @classmethod
    def deal(cls, str):
     y,m,d= map(int, str.split('-'))
     return cls(y,m,d) #return exp(y,m,d)

    def get_date(self):
     print("年份:%s" % self.y)

     print("月份:%s" % self.m)

     print("某日:%s" % self.d)

# a=exp(2019,08,02)
# a.get_date()
resu = exp.deal('2019-08-02') #接收y-m-d 类型的日期，resu=exp(2019,08,02)
resu.get_date()

print('======================================================')
print(isinstance([1,2,3],(list)))


