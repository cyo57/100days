# -*- coding:UTF8 -*-
from socket import socket
from time import sleep


def main():
    print('Connecting...')
    try:
        # 创建套接字对象, 默认IPv4和TCP
        client = socket()
        # 连接服务器 (IP:PORT)
        client.connect(('192.168.31.9', 6666))
        # 接收数据, 每次接收1024字节
        print(client.recv(1024).decode('utf8'))
        client.close()
    except:
        print('Connection refused. Please wait 2 secends.')
        sleep(2)

if __name__ == '__main__':
    while True:
        main()
