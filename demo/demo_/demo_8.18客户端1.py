import socket


def clint():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #建立连接
    s.connect(('127.0.0.1',9999))
    print(s.recv(1024).decode('utf_8'))
    for i in range(3):
     data=input('请输入:')
     s.send(data.encode())
     print(s.recv(1024).decode('utf_8'))
    s.send(b'exit')
    s.close()

if __name__=='__main__':
    clint()