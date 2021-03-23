import functools
import time
from functools import reduce

def perfomance(prefix):
 def new_fun(f):
    def fn(*args,**kw):
        start_time = time.time()
        r=f(*args,**kw)
        end_time = time.time()
        exe_time = (end_time - start_time)*1000 if prefix=='ms' else end_time-start_time
        print('call %s() in %f%s'%(f.__name__,exe_time,prefix))
        return r
    return fn
 return new_fun

@perfomance('ms')
def factorial(n):
    time.sleep(1)
    return reduce(lambda x,y:x*y,range(1,n+1))
print(factorial(10))

print("===================================================")

def f1(x):
    pass
print(f1.__name__)
print("===================================================")
def new_fn(f):
    # @functools.wraps(f)
    def fn(x):
        print('call...')
        return f(x)
    return fn
@new_fn
def f2(x):
    pass
print(f2.__name__)

print("===================================================")
print(int ('1001',base=2))


def int2(x):
    return int(x,base=2)
print(int2('1001'))
print("===================================================")
int2=functools.partial(int,base=2)
print(int2('1001'))

print("===================================================")

def f_cmp(x,y):
    if x[0].lower()<y[0].lower():
        return -1
    if x[0].lower()>y[0].lower():
        return 1
    return 0
#from functools import  cmp_to_key
print(sorted(['bob','about','Zoo','Credit'], key=functools.cmp_to_key(f_cmp)))
print("===================================================")

sorted_ignore=functools.partial(sorted,key=functools.cmp_to_key(f_cmp))
print(sorted_ignore(['bob','about','Zoo','Credit']))

print("===================================================")

class Person:
 pass
case_one=Person()
case_one.name='Xiao ming'
case_two=Person()
case_two.name='Li hua'

L1=[case_one,case_two]

# def f_cmp(p1,p2):
#     if p1.name>p2.name:
#         return 1
#     if p1.name<p2.name:
#         return -1
#     return 0
# L2=sorted(L1, key=functools.cmp_to_key(f_cmp))
L2=sorted(L1,key=lambda x:x.name)

for i in range(0,len(L1)):
 print(L2[i].name)