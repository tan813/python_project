def fir(func2):#此处func2指向warp1()
    print(2)
    def warp2(*args,**kwargs):
        print(3)
        func2(*args,**kwargs)
        print(6)
    return warp2

def sec(func1):#此处func1指向aa()
    print(1)
    def warp1(*args,**kwargs):
        print(4)
        func1(*args,**kwargs)
        print(5)
    return warp1

#装饰器函数在被装饰函数定义好后立即执行，所以在aa()调用前sec()、fir()函数已经执行，输出1、2
@fir    #sec = fir(sec) 调用sec/wrap1==调用fir/wrap2 }
        #                                              ==>  aa<==>wrap2
@sec    #aa = sec(aa)  调用aa==调用sec/即wrap1    }
def aa(c):
    print(c)
aa('最里边')