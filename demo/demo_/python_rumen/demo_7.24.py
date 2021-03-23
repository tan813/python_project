import dictionary as dictionary

a='python'
b=''
print('hello',a and 'world')
print('heloo',b and 'world')
print('============================================================')

L=['Amada','Lisa','Nick']
L.append('Bob')
L.insert(1,'Kike')
print(L)
print('============================================================')

L=['Amada','Lisa','Nick']
L.pop()
print(L)
print('============================================================')

L=['Amada','Lisa','Nick']
L.pop(1)
print(L)
print('============================================================')

T=('Amada')
T1=('Amada',)
print(T)
print(T1)
print('============================================================')

T=(1,2,3,['a','b'])
L=T[3]
L[0]='c'
L[1]='d'
print(L)
print(T)
print('============================================================')

num=(1,2,4,5)
num=num[:2]+(3,)+num[2:]
print(num)
print('============================================================')

T = ('aa','bb','cc','dd','ee')
print(T[4])
print(T[4:])
print(id(T))
print('============================================================')

dict = {('Name'): 'Zara', 'Age': 7, 'Class': 'First'}
key=sorted(dict.keys())
print(key)
dict['School']='Amid'
b=dict.fromkeys(dict,'ture')
print(b)
print(dict.get('Class'))
del dict['School']
print(dict)
dict.clear()
print(dict)
del dict
print('============================================================')

dict1 = {'a': [1, 2]}
print(dict1['a'][0])
print('============================================================')
from pip._vendor.distlib.compat import raw_input

dictionary = {}
flag = 'a'
pape = 'a'
off = 'a'
while flag == 'a' or 'c' :
    flag = raw_input("添加或查找单词 ?(a/c)")
    if flag == "a" :                             # 开启
        word = raw_input("输入单词(key):")
        defintion = raw_input("输入定义值(value):")
        dictionary[str(word)] = str(defintion)  # 添加字典
        print ("添加成功!")
        pape = raw_input("您是否要查找字典?(a/0)")   #read
        if pape == 'a':
            print (dictionary)
        else :
            continue
    elif flag == 'c':
        check_word = raw_input("要查找的单词:")  # 检索
        for key in sorted(dictionary.keys()):            # yes
            if str(check_word) == key:
                print ("该单词存在! ",key +":"+ dictionary[key])
                break
            else:                                       # no
                off = 'b'
        if off == 'b':
            print ("抱歉，该值不存在！")
    else:                               # 停止
        print ("error type")
        break
