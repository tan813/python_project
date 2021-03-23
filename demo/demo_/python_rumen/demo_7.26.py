from pip._vendor.distlib.compat import raw_input

with open ('a.txt','r') as f:
    print(f.read())
print("===========================================================")
b = open("b.txt", "w+")
b.write('www.runoob.com')
print(b.tell())
print (b.read())#在 write 内容后，直接 read 文件输出会为空，是因为指针已经在内容末尾。
# b.close()
# c=open('b.txt','r')
# print(c.read())
b.seek(0,0)
c=open('b.txt','r')
print(c.read())
print("===========================================================")

# weekday=['mon','tue','wed','thu','fri','sat','sun']
# x=raw_input("请输入星期：")
# if x in weekday:
#     print('input ok')
# else:
#     print('input error')
print("===========================================================")

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print (x[0] + ':', x[1])

print("===========================================================")
def fun (name='World'):
    print('Hello',name)
fun()
fun('Nick')

print("===========================================================")
def  fun (*num):
    sum=0
    for x in num:
        sum=sum+x
    return sum/len(num)
print(fun(1,2,3,4,5))
print("===========================================================")
def fun(str):
   str1= str[:1].upper()+str[1:]
   return str1
print(fun('sedr'))

print("===========================================================")
for i in range(1,101):
    if i%7==0:
        print(i,end=' ')

print("===========================================================")
L=['Adam','Lisa','Nick']
for index,name in enumerate(L):
    print(index ,'-', name)
print("===========================================================")
L=['Adam','Lisa','Nick','Paul']
for index,name in zip(range(1,len(L)+1),L):
    print (index,'-',name)
print("===========================================================")
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum=0
for x in d.values():
    sum=sum+x
print(sum/len(d))
# for key in d:
#     sum=sum+d[key]
# print(sum/len(d))
print("===========================================================")
a=[x*x for x in range(1,11)]
print(a)
a=[x*(x+1) for x in range(1,101,2)]
print(a)
print("===========================================================")
def toUppers(L):
    return [x[:1].upper()+x[1:] for x in L if isinstance(x,str)]

print (toUppers(['hello', 'world', 101]))
print("===========================================================")
print([100*m + 10*n + p for m in range(1,10) for n in range(0,10) for p in range(0,10) if m==p])

