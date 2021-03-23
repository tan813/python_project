# import time
# from multiprocessing import cpu_count
# from threading import current_thread, Thread, Lock,local
#
# #以函数的方式创建线程
# def loop():
#     print('thread %s is running...' % current_thread().name)
#     n=0
#     while n<5:
#         n=n+1
#         print('thread %s >>> %s'%(current_thread().name,n))
#         time.sleep(0.1)
#     print('thread %s ended.'%current_thread().name)
#
#
# print('thread %s is running...' % current_thread().name)
# t=Thread(target=loop,name='LoopThread1')
#
# t.start()
# t.join()
#
# print('thread %s ended.'%current_thread().name)
# print('=======================================================================')
#
# #以类的方式创建线程
# class MyThread(Thread):
#     def __init__(self,func,name):
#         super(MyThread, self).__init__()
#         self.func=func
#         self.name=name
#     def run(self):
#         self.func()
# def loop():
#   print('thread %s is running...' % current_thread().name)
#   n=0
#   while n<5:
#       n=n+1
#       print('thread %s >>> %s'%(current_thread().name,n))
#       time.sleep(0.1)
#   print('thread %s ended.'%current_thread().name)
#
# if __name__=='__main__':
#     print('thread %s is running...' % current_thread().name)
#     thread_1=MyThread(loop,'LoopThread')
#     thread_1.start()
#     thread_1.join()
#     print('thread %s ended.' % current_thread().name)
#     print('===========================================================================')
#
# #创建lock锁确保同一时刻最多只有一个线程执行change_it
# # 假定这是你的银行存款:
# balance = 0
# lock=Lock()
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         lock.acquire()
#         try:
#          change_it(n)
#         finally:
#             lock.release()
# t1 = Thread(target=run_thread, args=(5,))
# t2 = Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
#
# print('===========================================================================')
#
# #ThreadLocal(单个线程内所有函数的全局变量)
# global_data =local()
#
# def show():
#     print (current_thread().name, global_data.str)
#
# def thread_cal(name):
#     global_data.str=name
#     show()
#
# threads = []
# for i in range(10):
#     threads.append(Thread(target=thread_cal,args=(i,),name='thread-'+str(i)))#name参数为子线程名字
#     threads[i].start()
#
