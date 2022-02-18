# Python-100-days

## 基础

### 语言元素

### 分支结构

### 循环和逻辑构造

### 模块和函数

### 字符串和常用数据结构

### 面向对象基础

### 面向对象进阶

### tkinter和pygame

### 文件和异常

### 字符串和正则表达式

### 进程和线程

> day13

#### 概念

每个进程都有自己的地址空间、数据栈以及其他用于跟踪进程执行的辅助数据，操作系统管理所有进程的执行，为它们合理的分配资源。

必须通过进程间通信机制（IPC，Inter-Process Communication）来实现数据共享，具体的方式包括管道、信号、套接字、共享内存区等。

#### Python的多进程

Unix和Linux操作系统提供了`fork()`系统调用穿件进程, 调用函数的是父进程, 拷贝一个子进程且拥有自己的PID, Python的os模块提供了`fork()`.

但由于Windows没有`fork()`, 因此如果需要跨平台, 可以使用multiprocessing模块的`Process`类创建子进程, 并且该模块提供了高级的封装, 例如批量启动进程的进场池`Pool`, 进程间通信的队列`Queue`和管道`Pipe`等

如果没有多进程或者多线程, Python的代码只能按顺序一点点执行, 即使两个毫不相关的函数, 也需要队列执行, 显然很不合理也没有效率.

```python
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python.pdf', ))
    p2 = Process(target=download_task, args=('Peking.avi', ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # Process创建进程对象, target传入函数, args传递参数
    # Process对象的start()方法启动进程, join方法等待进程结束
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
```

以上代码是多进程的简单使用方法, 也可以使用subprocess模块中的类和函数创建和启动子进程, 然后通过管道和子进程通信.

此处不展开学习, 重点在于学习不同进程间的通信

#### Python的多线程

早起的Python中引入了thread模块 (现更名为_thread) 来实现多线程, 但该模块过于底层, 且很多功能无提供, 因此目前多线程推荐使用threading模块. 该模块提供了更好的面向对象的封装.

```python
from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('Python.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Peking.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()
```

我们可以直接使用threading模块的`Thread`类创建线程, 之前学习过面向对象的继承 (大概在day10~11), 可以从已有的类创建新类, 因此我们可以继承`Thread`类创建自定义类

```python
from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
```

因为多个线程可以共享进程的内存空间, 因此实现通信比多进程更容易, 例如共享全局变量. 但多个线程共享一个**资源**时, 很可能产生不可控的结果, 从而程序失效甚至崩溃. 如果一个资源呗多个线程竞争 (临界资源) 时, 对"临界资源"需要加以保护, 否则资源将处于混乱
