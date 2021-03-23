import operator
import time

dict={'name':'Zara','Age':'7','Class':'First'}
print ("dict[Age]:",dict['Age'],"dict[Class]:",dict['Class'])
dict1={'name':'Sara','Age':'6','Class':'Fice'}
print(operator.eq(dict,dict1))

ticks =time.time()
print(ticks)
localtime=time.localtime(time.time())
print("本地时间为：",localtime)
localtime=time.asctime(time.localtime(time.time()))
print("本地格式化时间为：",localtime)
print (time.strftime("%Y-%m-%d %H:%M:%S"),time.localtime())

def printme(str):
    print(str)
    return
printme("被调用啦！")
printme("再次调用")

def change(a):
    a=10
    return a

b=2
change(b)
print(b)