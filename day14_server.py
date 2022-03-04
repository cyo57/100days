from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime
from threading import Thread

def _log(s):
    _isLog = True
    if _isLog:
        print(s)



def main():
    # 创建并指定服务
    # 指定IPv4和TCP
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 绑定IP和端口
    server.bind(('192.168.31.9', 6666))
    # 监听开启
    # 参数为连接队列大小
    server.listen(512)
    print('Server ON.')
    while True:
        # 接受客户端连接并作出处理 (提供服务)
        # accept是阻塞方法, 无连接不执行, 返回元组, 第一个元素是客户端对象, 第二个元素是连接到服务器的地址 (IP:PORT)
        client, addr = server.accept()
        print(str(addr) + ' connected.')
        # 发送数据
        client.send(str(datetime.now()).encode('utf8'))

def main_thread():
    class DateHandler(Thread):
        def __init__(self, client) -> None:
            super().__init__()
            self.client = client
        
        def run(self):
            self.client.send(str(datetime.now()).encode('utf8'))
            self.client.close


    server = socket()
    server.bind(('192.168.31.9', 6666))
    server.listen(512)
    print('Server ON.')
    while True:
        client, addr = server.accept()
        _log(addr)
        DateHandler(client).start()


if __name__ == '__main__':
    #main()
    main_thread()