import socketserver
class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
        #处理连接1024kb数据，进行解码
            data = self.request.recv(1024).decode()
            if data == 'exit':
                print('客户端发送完成，断开连接')
                break
            print('接受到客户端：%s 发送的信息：%s' % (self.client_address, data))
            res = data.upper()
            # 发送回客户端
            self.request.send(res.encode())

        self.request.close()

hostaddress=('127.0.0.1',8889)
server=socketserver.ThreadingTCPServer(hostaddress,MyHandler)
print('启动socket服务，持续监听中')
server.serve_forever()




