import codecs
import csv
from itertools import islice

# 读取本地csv文件
datas = csv.reader(codecs.open('./test.csv', 'r', 'gb2312'))
# 存放读取数据
case = []
for data in islice(datas, 1, None):
    case.append(data)
print(case)