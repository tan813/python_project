import json
# 从json文件数据读出Str数据再转换成python结构
# loads()函数
def fun1():
    with open ("./demo1_1.json","r") as f:
        # data为str类型数据
        data = f.read()
    print(type(data))
    user_list = json.loads(data)
    print(user_list)

# json文件数据转换成python结构
# loads()函数
def fun2():
    with open ("./demo1_1.json","r") as f:
        user_list = json.load(f)
    print(user_list)

fun1()
fun2()
