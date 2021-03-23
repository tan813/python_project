import random
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager
from queue import Queue
#发送任务的队
task_queue=Queue()
#接收结果的队列
result_queue=Queue()

class QueueManager(BaseManager):
    pass
def get_task():
    return task_queue
def get_result():
    return result_queue

def run():
  #将两个Queue注册到网络上，暴露给其他进程（主机），注册后获得网络队列，相当于本地队列的映像
  QueueManager.register('get_task_queue',callable=get_task)
  QueueManager.register('get_result_queue',callable=get_result)

  #建立一个对象实例manager，绑定端口和验证口令
  manager=QueueManager(address=('192.168.0.101',5000),authkey=b'abc')

  #启动实例，即启动管理manager，监管信息通道
  manager.start()

  #通过管理实例的方法获得通过网络访问的Queue对象，即再把网络队列实体化成可以使用的本地队列
  task=manager.get_task_queue()
  result=manager.get_result_queue()

  #创建任务到 “本地”队列中，自动上传任务到网络队列中，分配给任务进程进行处理
  for i in range(10):
      n = random.randint(0, 10000)
      print('Put task %d...' % n)
      task.put(n)

  # 从result队列读取结果:
  print('Try get results...')
  for i in range(10):
      r = result.get(timeout=10)
      print('Result: %s' % r)
  # 关闭:
  manager.shutdown()
  print('master exit.')

if __name__=='__main__':
    freeze_support()
    run()