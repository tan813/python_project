import time
# from functools import reduce
#
#
# def cal_sum(lst):
#     def lazy_sum():
#         return sum(lst)
#     return lazy_sum
# f=cal_sum([1,2,3,4])
# print(f)
# print(f())
#
# def cal_prod(lst):
#     def lazy_prod():
#         def f(x,y):
#             return x*y
#         return reduce(f,lst,1)
#     return lazy_prod
# x=cal_prod([1,2,3,4])
# print(x())
#
# print("===========================================================")
# # def count():
# #     fs = []
# #     for i in range(1, 4):
# #         def f():
# #             return i*i
# #         fs.append(f)
# #     return fs
# # f1, f2, f3 = count()
# # print(f1(), f2(), f3())
#
# print (list(filter(lambda s:s and len(s.strip())>0, ['test', None, '', 'str', '  ', 'END'])))
#
# print(reduce(lambda a,b:a*b,[1,2,3,4]))
#
# print("===========================================================")
#
# def new_fn(f):
#     def fn(x):
#         print('call')
#         return f(x)
#     return fn
#
# @new_fn
# def f1(x):
#     return x*2
#
#
# print(f1(6))
# print(f1(7))
#
# print("===========================================================")
# def f2(x):
#     return x*2
# def new1_fn(f,x):
#     print('call')
#     return f(x)
#
# f6=new1_fn(f2,6)
# f7=new1_fn(f2,7)
# print(f6)
# print(f7)
# print("===========================================================")
# def fun(*args):
#     prod=1
#     for x in args:
#         prod=prod*x
#     return prod
# print(fun(1,2,3,4,5,6))

print("===========================================================")
def new_fun(f):
    def fn(*args):
        start_time=time.time()
        r=f(*args)
        end_time=time.time()
        exe_time = (end_time - start_time) * 1000
        print("time is %d ms" % exe_time)
        return r
    return fn

@new_fun #add=new_fun(add)
def add(*args):
    sum=0
    for x in args:
        sum=sum+x
    time.sleep(1)
    return sum
print(add(1,2,3,4))
# if __name__=='__main__':
#     add(1,2,3,4)





