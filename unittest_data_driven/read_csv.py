import csv

# 读取本地csv文件
case = []
with open('./test.csv', 'r') as csvFile:
    datas = csv.reader(csvFile)
    next(datas)
    for row in datas:
        # case.append(row)
        print(row[1])