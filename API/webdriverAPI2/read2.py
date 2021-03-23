# 读取本地csv文件
import codecs
import csv
from itertools import islice

# 读取本地csv文件
# data = csv.reader(codecs.open('./test.csv', 'r', 'utf_8_sig'))
data = csv.reader(codecs.open('./test.csv', 'r', 'gbk'))

# 存放用户数据
users = []

# 循环输出每行信息
for line in islice(data, 1, None):
    users.append(line)

# 打印
print(users)
