import json

dict = [{'usename': 'user', 'password': 'password123'},
        {'usename': 'user1', 'password': 'password1234'}]
# 将python dict类型数据转成str类型数据，然后写入json文件
# dumps()函数
def fun1():
    data = json.dumps(dict)
    # data为str类型数据
    print(type(data))
    with open("./demo1_2.json","w") as f:
        f.write(data)

# 直接将dict类型数据转成str类型数据并写入json文件
def fun2():
    with open("./demo1_2.json","w") as f:
        json.dump(dict,f)

fun2()