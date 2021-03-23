import socket
import threading
import time


def serve():
  #创建一个socket
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  #监听端口
  s.bind(('127.0.0.1',9999))
  s.listen(2)#参数指定等待连接的最大数量
  print('Waiting for connection...')

  while True:
      sock,addr=s.accept()#等待并返回一个客户端连接
      #创建新线程来处理TCP连接
      t=threading.Thread(target=tcplink,args=(sock,addr))
      t.start()



def tcplink(s_ock,a_ddr):
    print('Accept new connection from %s:%s...' % a_ddr)
    s_ock.send(b'welcome!')
    while True:
        data=s_ock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf_8')=='exit':
            break
        s_ock.send(('Hello,%s!'%data.decode('utf_8')).encode('utf_8'))
    s_ock.close()
    print('connection from %s:%s closed' % a_ddr)



if __name__=='__main__':
    serve()