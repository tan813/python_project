import json
import os
#
# with open('a.txt','r') as f:
#  print(f.read(2))
#  f.seek(0,0)
#  print('====================================')
#
#  print(f.readline())
#  f.seek(0,0)
#  print('====================================')
#
#  print(f.readlines())
#  f.seek(0, 0)
#  print('====================================')
#
#  for line in f.readlines():
#      print(line.strip())
#  print('====================================')
#
#  with open('E:\\111.jpg','rb') as j:
#      print(j.read())
#
#  print('=================================================')
#  from io import StringIO
#  f=StringIO()
#  f1=StringIO('Hello')
#  f.write('hello')
#
#  print('此时指针位置为：%d'%f.tell())
#  print(f.read())
#  #f.getvalue()则会初始化指针位置为0
#
#  print('此时指针位置为：%d'%f1.tell())
#  print(f1.read())
#
#  print('=================================================')
#  from io import BytesIO
#  f=BytesIO('中文'.encode('utf-8'))
#  print(f.read())
#  print(f.getvalue())
#
# import os
# print(os.environ)#查看环境变量
# print(os.environ.get('PATH'))#获取某个环境变量的值
#
# print('=================================================')
#
#
# os.mkdir('E:\\m_down\\ss')
# os.rmdir('E:\\m_down\\ss')
#
#
# print([x for x in os.listdir('D:\\Users\\lenovo\\Python_project\\demo\\demo_') if os.path.isdir(x)])
#
# print([x for x in os.listdir(os.path.abspath('.'))])
#
# print([x for x in os.listdir('.') if os.path.isfile(x)])
#
# a=os.path.splitext('D:\\Users\\lenovo\\Python_project\\demo\demo_a.txt')
# print(a[1])
#
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.txt'])
#
# print(os.path.abspath('.'))#查看当前目录绝对路径

# print('==========查找当前目录和子目录下所有文件中包含指定字符串的文件名（方法一）===========================================================')
# def find(f_path, s_tr):
#     os.chdir(f_path)#改变工作目录到当前目录,否则不能输出子目录中的文件名
#     for x in os.listdir('.'):
#         n = os.path.join(f_path, x)
#         if os.path.isfile(n) and s_tr in n:
#             print(x)
#         if os.path.isdir(n):
#             print('子目录路径为:%s'%n)
#             find(n, s_tr)
#
# # s = input('Enter one string: ')
# d=os.path.abspath('.')
# s='7'
# find(d,s)
#
# #（一）：d='D:\Users\lenovo\Python_project\demo\demo_'报错
# #原因：'\'含有转义字符的意思，要使得 '\'不被解读为转义字符
# #①：改为d=r'D:\Users\lenovo\Python_project\demo\demo_'
# #②：'\'改为'\\'
# #③：'\'改为'/'
# #(二)：os..path.isfile()、os.path.isdir(参数均为绝对路径）
# print('=======查找当前目录和子目录下所有文件中包含指定字符串的文件名（方法二）================================================================')
#
# str=input('请输入要查找的字符串：')
# for dirpath,dirnames,filenames in os.walk(r'D:\Users\lenovo\Python_project\demo\demo_'):
#     for filename in filenames:
#         if str in filename:
#             print(filename)
#
#
# print('=====================================================================')
# import pickle
# d=dict(name='Bob',age='20',score='88')
# p=pickle.dumps(d)
# with open('dump.txt','wb') as f:
#  f.write(p)
# # with open ('dump.txt','wb') as f:
# #     pickle.dump(d,f)
#
# with open ('dump.txt','rb') as f:
#     b=f.read()
#     d=pickle.loads(b)
#     print(d)
# # with open ('dump.txt','rb') as f:
# #     d=pickle.load(f)
# # print(d)

print('====================================================================')

# d=dict(a=1,b=2)
# print(json.dumps(d))
# d='{"age":20,"name":"Bob"}'
# print(json.loads(d))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
# def Student2dict(std):
#     return {
#         'name':std.name,
#          'age':std.age,
#          'score':std.score
#     }
s = Student('Bob', 20, 88)

# print(json.dumps(s,default=Student2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__))

print('========================================================')
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

print('========================================================')
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)