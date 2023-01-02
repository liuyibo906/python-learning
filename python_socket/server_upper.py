# email liuyibo906@163.com
# 时间 2023/1/2 10:51
#可以多线程处理
import socket
import threading
def deal(link,client):
    while True:
        # 处理连接1024kb数据，进行解码
        data = link.recv(1024).decode()

        if data == 'exit':
            break
        print('接受到客户端：%s 发送的信息：%s' % (client, data))

        res = data.upper()
        # 发送回客户端
        link.sendall(res.encode())

    link.close()

#服务的IP地址和端口号
hostaddress=('127.0.0.1',8889)
#默认使用IPV4,使用TCP协议
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定服务地址
sk.bind(hostaddress)
#设置监听,最多5个人线程
sk.listen(5)
print('启动socket服务，等待客户端连接')
while True:
    #连接上返回
    conn,clientaddress=sk.accept()
    xd=threading.Thread(target=deal,args=(conn,clientaddress))
    xd.start()



