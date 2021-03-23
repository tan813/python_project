import random
import time
import os
from multiprocessing import Process,Pool,Queue


def action(a,b):
 for i in range(30):
     print(a,b)
     time.sleep(0.1)
if __name__=='__main__':
    jc1=Process(target=action,args=('进程一',0))
    jc2=Process(target=action,args=('进程二',1))

    jc1.start()
    jc2.start()

    jc1.join()
    jc2.join()
    print('jc1、jc2任务都已经执行完毕')
    print('==================================================================')


def run(name):
    print('Run child process %s (%s)...,my parent process is %s'%(name,os.getpid(),os.getppid()))

if __name__=='__main__':
    print('Parent process %s.'%os.getpid())
    p=Process(target=run,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    print('==================================================================')

def long_time_task(name):
    print('Run task %s (%s)...'%(name,os.getpid()))
    start=time.time()
    time.sleep(3)
    end=time.time()
    print('Task %s runs %.2f seconds.'%(name,(end-start)))

if __name__=='__main__':
    print('Parent process %s.'%os.getpid())
    p=Pool(4)#进程池最大运行数为4
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    print('==================================================================')

def foo(aa):
    while True:
        if not aa.empty():
           ss = aa.get()  # 管子的另一端放在子进程这里，子进程接收到了数据
           #ss=aa.get(True,2)
           #aa.get(True,timeout)
          #如果block使用默认值True，且没有设置timeout（单位秒），消息列队如果为空，此时程序将被阻塞（停在读取状态）
          # 直到从消息列队读到消息为止，如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出"Queue.Empty"异常；
           print('子进程已收到数据...')
           print(ss)  # 子进程打印出了数据内容...
        else:
            break

if __name__ == '__main__':  # 要加这行...

    tx = Queue()  # 创建进程通信的Queue，你可以理解为我拿了个管子来...
    jc = Process(target=foo, args=(tx,))  # 创建子进程
    print('主进程准备发送数据...')
    tx.put('有内鬼，终止交易！')  # 将管子的一端放在主进程这里，主进程往管子里丢入数据↑
    jc.start()  # 启子子进程
    jc.join()
    print('===================================================================')

def write1(aa):
    for value in 'ABCD':
        print('Put %s to queue'%value)
        aa.put(value)
        time.sleep(0.2)
def write2(aa):
    for value in 'EFGH':
        print('Put %s to queue'%value)
        aa.put(value)
        time.sleep(0.2)

def read (aa):
    while True:
        if not aa.empty():
            value=aa.get()
            print('Get %s from queue'%value)
            time.sleep(0.2)
        else:
            break

if __name__=='__main__':
    q=Queue()
    w1=Process(target=write1,args=(q,))
    w2=Process(target=write2,args=(q,))
    r=Process(target=read,args=(q,))

    w1.start()
    w1.join()
    w2.start()
    w2.join()
    r.start()
    r.join()

    print('数据读写完毕！')