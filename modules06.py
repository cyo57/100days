def test():
    global a    # 类似于import, 从全局变量引入
    print('Hello World!')

if __name__ == '__main__':
    a = 1
    print('不运行')