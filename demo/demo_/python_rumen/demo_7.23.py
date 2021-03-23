s_tr=lambda str:print(str)
n_um=lambda num1,num2:num1+num2
s_tr("lambda")
print("num1+num2的值是：%d"%(n_um(10,20)))
print("------------------------------------------------------------------")

def funx(x):
 def funy(y):
    return x*y
 return funy
print(funx(7)(8))
print("------------------------------------------------------------------")

def funx(x):
    def funy(y):
        return x*y
    return funy(8)
print(funx(7))
print("------------------------------------------------------------------")

def add(x,y):
    return x+y
def add_twice(add,x,y):
    return add(add(x,y),add(x,y))
print(add_twice(add,5,10))
print("------------------------------------------------------------------")

print(45678+0x12fd2)
print(100<99)
print("------------------------------------------------------------------")

s = 'Python was started in 1989 by "Guido".\nPython is free and easy to learn.'
print (s)
print("------------------------------------------------------------------")

print (r'''"To be, or not to be": that is the question.
      Whether it's nobler in the mind to suffer.''')
print("------------------------------------------------------------------")

print(r'''XiaoMing say:"I'm ok!" ''')
print("------------------------------------------------------------------")

print(10/4)
print(10//4)