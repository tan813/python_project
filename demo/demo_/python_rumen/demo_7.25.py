import calendar
import datetime
import os
import time
print(datetime.datetime.now() - datetime.timedelta(days=1))#计算昨天的日期
T1=time.time()
T2=time.asctime(time.localtime())
T3=time.localtime()
T4=time.strftime("%H:%M:%S",time.localtime())
T5=time.strftime("%H:%M:%S")
print(T2)
print(T3)
print(T4)
print(T5)
print("===========================================================")

cal=calendar.month(2019,7)
print(cal)
print("===========================================================")

i=datetime.datetime.now()
print("当前时间是：%s"%i)

print("===========================================================")
def reverse(Listinput):
    Newlist=[]
    for i in range( len(Listinput)):
        Newlist.append(Listinput.pop())
    print(Newlist)
reverse([1,2,3,4,5])
print("===========================================================")

def reverse(li):
    for i in range(0, int(len(li)/2)):
        li[i], li[-i - 1] = li[-i - 1], li[i]
l = [1, 2, 3, 4, 5]
reverse(l)
print(l)
print("===========================================================")

l = [1, 2, 3, 4, 5,6]
l[0],l[-1]=l[-1],l[0]
print(l)
print("===========================================================")

print(dir(time))
print("===========================================================")

for x in range(2,10,2):
    print(x,end=' ')
print('\n')
print("===========================================================")

f=open("a.txt",'w')
f.write("www.baidu.com\nwww.jd.com")
f.close()

fi=open('a.txt','r')
str=fi.read()
print(str)
fi.close()
print("===========================================================")
# 打开一个文件
fo = open("a.txt", "r+")
str = fo.read(10)
print("读取的字符串是 : ", str)

# 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)

# 把指针再次重新定位到文件开头
position = fo.seek(16, 0)
str = fo.read(6)
print("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()
print("===========================================================")

# os.rename('a.txt','b.txt')
# os.remove('b.txt')
# os.mkdir('test')
# print(os.getcwd())
# os.chdir('test')
# print(os.getcwd())

# os.rmdir('test')