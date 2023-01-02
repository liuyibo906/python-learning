# email liuyibo906@163.com
# 时间 2023/1/2 10:53
import socket

serveraddress=('127.0.0.1',8889)

sk=socket.socket()

sk.connect(serveraddress)

while True:
    sss=input('请发送消息：')

    sk.sendall(sss.encode())
    if sss=='exit':
        break
    answer=sk.recv(1024).decode()

    print('收到服务器发送的信息：%s' % answer)

sk.close()