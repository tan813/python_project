import re

# a=re.split(r'[\,\s\d\;]+','a,,b,;;c 3  d')
# print(a)
#
# print('============================================================')
# m = re.match(r'(\d)', '1222').groups()
# print(m)
#
# a=re.match(r'^(\d*?)(0*)$','102300').groups()
# print(a)
#
#
# re_num=re.compile(r'^(\d*?)(0*)$')
# a=re_num.match('102300').groups()
# print(a)
line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.group(0))
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")


# pattern = "\w+\@\w+.*(\w)\.com"  # 匹配邮箱
# mt = re.match(pattern, "luosongchao@xxx.yyy.xadad.com")
# print(mt.groups())
# print(mt.group())

# pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
# m = pattern.match('Hello World Wide Web')
# print(m.group())# 返回匹配成功的整个子串
# print(m.groups())#返回匹配成功的子串分组
# print(m.span(0))#返回匹配成功的整个子串的索引
# print(m.span(1))## 返回第一个分组匹配成功的子串的索引
#
# pattern1 = re.compile(r'([a-z]+.*) ([a-z]+)', re.I)
# m = pattern1.match('Hello World Wide Web')
# print(m.group())
# print(m.groups())

num=re.compile(r'\d+')
a=num.match('23fuddd12')
b=num.search('d23fuddd12')
c=num.findall('d23fuddd12')
print(a.group())
print(b.group())
print(c)