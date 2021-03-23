# import itertools
# from contextlib import contextmanager
# #①itertools模块
# #count()、cycle()、repeat()无限迭代自然数、序列、一个元素
#
# natuals= itertools.count(1,2)#取奇数序列
# ns=itertools.takewhile(lambda x:x<=9,natuals)
# print(list(ns))
#
#
# natuals= itertools.count(1)#取自然数序列
# ns=itertools.takewhile(lambda x:x<=5,natuals)
# print(list(ns))
#
#
# print('==================================================')
# def pi(N):
#     ' 计算pi的值 '
#     # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
#     natuals=itertools.count(1,2)
#     # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
#     ns=list(itertools.takewhile(lambda  x:x<=2*N-1,natuals))
#     # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
#     sum=0
#     for i in range(N):
#      if i%2==0:
#          sum=sum+4/ns[i]
#      else:
#          sum=sum+(-4/ns[i])
#     # step 4: 求和:
#     return sum
# print(pi(10000))
# print('=====================================================')
#②contextlib模块
# from contextlib import contextmanager
#
#
#
#
# class Query:
#     def __init__(self,name):
#         self.name=name
#     def query(self):
#         print('Query info about %s...'%self.name)
# @contextmanager
# def create_query(name):
#     print('Begin')
#     yield Query(name)
#     print('End')
#
# with create_query('Bob') as q:
#     q.query()
#
# print('========================================================')
# #某段代码执行前后自动执行特定代码
# @contextmanager
# def tag(name):
#     print('<%s>'%name)
#     yield
#     print('<%s>'%name)
#
# with tag('hl'):
#     print('hello')
#     print('world')
#
# print('========================================================')
#常用第三方模块 Pillow
from PIL import Image,ImageFilter
im=Image.open('111.jpg')
#获取图像尺寸
w,h=im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg','jpeg')
#应用模糊滤镜
im=Image.open('111.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg')