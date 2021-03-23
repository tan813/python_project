def fir(func2):
    print(2)
    print(func2)
    def warp2(*args,**kwargs):
        print(3)
        func2(*args,**kwargs)
        print(6)
    return warp2
def sec(func1):
    print(1)
    print(func1)
    def warp1(*args,**kwargs):
        print(4)
        func1(*args,**kwargs)
        print(5)
    return warp1
@fir
@sec
def aa(c):
    print(c)
aa('最里边')
