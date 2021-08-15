import csv

# 读取本地csv文件
case = []
with open('./test.csv', 'r') as csvFile:
    datas = csv.reader(csvFile)
    for row in datas:
        case.append(row)
print(case)