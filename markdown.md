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

可以通过锁来防止竞争, 只有获取到锁的线程才能执行

```python
from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 必须获取到锁才能执行
        self._lock.acquire()
        try:
            # 计算存款后的余额
            new_balance = self._balance + money
            # 模拟受理存款业务需要0.01秒的时间
            sleep(0.01)
            # 修改账户余额
            self._balance = new_balance
        finally:
            # 释放锁
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
```

### 网络编程入门

#### TCP/IP 模型
网络通信协议通常由*互联网工程任务组* (IETF) 制定的. 所谓"协议"就是通信计算机双方遵从的约定, 例如建立连接 & 互相识别等. 网络协议三要素是 语法& 语义& 时序.
构成我们今天使用的Internet的基础是TCP/IP协议族, 就是一些列协议机器构成的通信模型, 称之为TCP/IP模型. 层次自底向上依次是 网络接口层& 网络层& 传输层& 应用层.

TCP全程传输控制协议, 它基于IP提供的寻址和路由服务而建立起来的端到端可靠传输的协议, TCP向使用者承诺三件事

- 数据不传丢, 不传错. (利用握手& 校验& 重传机制)
- 流量控制 (通过滑动窗口匹配数据发送者和接受者之间的传输速度)
- 拥塞控制 (通过RTT时间以及对滑动窗口的控制缓解网络拥塞)

#### 网络应用模式

- C/S 和 B/S, 此处C指Client, 通常指某个应用程序. B指Browser. 通过C或B都可以实现对S (Server) 的访问
- 去中心化, 通常没用固定的服务器或客户端, 所有应用的使用者都可以作为资源提供者或访问者

#### HTTP (超文本传输协议)

全程 Hyper-Text Transfer Proctol, Wiki Pedia上的解释是: 

简单来说, 通过HTTP我们可以获取网络上的 (基于字符) 资源, 开发中经会用到的网络API就基于HTTP来实现传输

#### JSON

JavaScript Object Notation 是一种轻量级的数据交换语言, 以易于人类阅读的文字 (文本) 为基础, 用来传输属性值或序列性的值组成的数据对象. 由于JSON是纯文本, 和XML一样适用于异构系统间的数据交换, 但JSON显然比XML更加的轻便和优雅

#### requests库

基于HTTP协议使用网络的第三方库, 其官网介绍: "Requests是惟一的一个非转基因的Python HTTP库, 人类可以安全享用." 总之, 使用requests可以方便的使用HTTP, 避免安全缺陷& 冗余代码& 重复发明轮子

`pip install requests`

如果用PyCharm作为IDE, 可以通过代码修复功能自动下载安装库

我们简单写了一个获取QQ信息的程序

```python
from threading import Thread
import requests

class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
    
    def run(self):
        filename = self.url[self.url.rfind('/'+1)]
        resp = requests.get(self.url)
        with open('~/' + filename, 'wb') as f:
            f.write(resp.content)


class GetHttp(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
    
    def run(self):
        resp = requests.get(self.url)
        print(resp.content)


def main():
    qqnum = '1342009839'
    url = 'https://api.muxiaoguo.cn/api/QqInfo?qq=' + qqnum
    resp = GetHttp(url).start()

if __name__ == '__main__':
    main()
```



#### TCP套接字

就是使用TCP协议提供的传输服务来实现网络通信的编程接口. 在Py中创建socket对象并制定type属性为SOCK_STREAM使用TCP套接字. 由于一台主机可能有多个IP, 且配置多个不同服务, 所以作为服务端, 需要创建套接字对象后绑定到指定的IP和端口. 此处端口并非是物理设备, 而是IP地址的扩展, 区分不同的服务. 例如HTTP跟80绑定, MySQL默认绑定3306. 端口的范围是0~65535, 而1024以下的称之为"著名端口",  (例如FTP& HTTP& SMTP) 等等.

下面代码实现一个提供日期的服务器

```python
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


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


if __name__ == '__main__':
    main()
```

下面代码实现一个客户端

```python
from socket import socket


def main():
    print('Connecting...')
    try:
        # 创建套接字对象, 默认IPv4和TCP
        client = socket()
        # 连接服务器 (IP:PORT)
        client.connect(('192.168.31.9', 6666))
        # 接收数据
        print(client.recv(1024).decode('utf8'))
        client.close()
    except ConnectionRefusedError:
        print('Connection refused.')


if __name__ == '__main__':
    main()
```



#### UDP套接字

传输层除去可靠的TCP之外, 还有一种非常轻便的传输协议叫用户数据报协议, 简称UDP. TCP和UDP都是端到端传输服务的协议, 只是UDP不对传输的可靠性和可达性作出承诺, 从而避免了TCP中握手和重传的开销, 所以在强调性能而不是数据完整性的场景中 (例如串流音视频), UDP可能是更好的选择.

#### 发送电子邮件

就像HTTP访问网站一样, 发邮件使用建立在TCP基础上的应用级协议SMTP, 它规定了邮件的发送者如何与发送邮件的服务器进行通信, Pthon中的smtplib模块将操作简化成了几个函数















```python
from socket import socket


def main():
    print('Connecting...')
    try:
        # 创建套接字对象, 默认IPv4和TCP
        client = socket()
        # 连接服务器 (IP:PORT)
        client.connect(('192.168.31.9', 6666))
        # 接收数据
        print(client.recv(1024).decode('utf8'))
        client.close()
    except ConnectionRefusedError:
        print('Connection refused.')


if __name__ == '__main__':
    main()
```



#### UDP套接字

传输层除去可靠的TCP之外, 还有一种非常轻便的传输协议叫用户数据报协议, 简称UDP. TCP和UDP都是端到端传输服务的协议, 只是UDP不对传输的可靠性和可达性作出承诺, 从而避免了TCP中握手和重传的开销, 所以在强调性能而不是数据完整性的场景中 (例如串流音视频), UDP可能是更好的选择.

#### 发送电子邮件

就像HTTP访问网站一样, 发邮件使用建立在TCP基础上的应用级协议SMTP, 它规定了邮件的发送者如何与发送邮件的服

### 图像和办公文档处理

Python标准库中虽然没有直接支持这些操作的模块, 但我们可以通过Python生态的第三方模块完成操作

#### 计算机图像相关知识

- 颜色
  通常我们会将一个颜色表示为一个RGB值或RGBA值 (A为Alpha通道, 他决定透过图像的像素, 也就是透明度)
- 像素
  最想单位就是单一颜色的小方格, 通常称为像素 (pixel)

#### Pillow操作图像

`pip install pillow`

Pillow中最重要的是Image类, 读取和处理都由这个类完成

```python
from PIL import Image
import requests

path = './res/image.png'

image = Image.open(path)
# image.format, image.size, image.mode
# image.show()

def img_crop():
    '''图像的裁剪'''
    rect = 80, 80, 160, 160
    image.crop(rect).show()

def img_thumb():
    '''图像的缩略图'''
    size = [300, 300]
    image.thumbnail(size)
    image.show()

def img_guido():
    '''图像的缩放和粘贴'''
    pass

if __name__ == '__main__':
    #img_crop()
    img_thumb()
```

#### 处理Word

利用python-docx库, 当然并非指MS Office软件创建的docx, 例如LibreOffice和OpenOffice都是免费的软件



## 进阶

### 重要点

#### 生成式 (推导式)

```python
prices = {
    'A': 199,
    'B': 200,
    'C': 185,
    'D': 300
}
priceNew = {key: value for key, value in prices.items() if value >= 200}
print(priceNew)
```

#### 嵌套的列表

```python
# 嵌套列表
def b():
    names = ['cyo57', 'hxert', '赵云', '关羽']
    courses = ['语文', '数学', '英语']
    # 录入四名学生 三门课的成绩
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for col, course in enumerate(scores):
            scores[row][col] = float(input(f'输入{name}的{course}成绩: '))
```

#### heapq模块 堆排序

```python
# heapq模块 (堆排序)
# 从列表中找出最大或最小的N个元素
# 解构堆(大根堆/小根堆)
import heapq
def c():
    list1 = [34, 56, 24, 76, 27, 84, 25, 74, 90]
    list2 = [
        {'name': 'A', 'shares': 100, 'price': 90},
        {'name': 'B', 'shares': 200, 'price': 60},
        {'name': 'C', 'shares': 300, 'price': 70}
    ]
    print(heapq.nlargest(100, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(3, list2, key=lambda x: x['price']))
```

#### 迭代工具 itertools模块

```python
# 迭代工具模块
import itertools
def d():
    # 产生ABCD全排列
    itertools.permutations('ABCD')	#(A,B,C,D) (A,B,D,C) (A,C,B,D)
    # 产生ABCDE五选三组合
    itertools.combinations('ABCDE', 3) #(A,B,C) (A,B,D) (A,B,E)
    # 产生ABCD和123的笛卡尔积
    itertools.product('ABCD', '123') #(A,1) (A,2) (A,3) (B,1)
    # 产生ABC的无限序列循环
    itertools.cycle(('A', 'B', 'C')) #A B C A B C

    for _ in itertools.product('ABCD', '123'):
        print(_)
```

#### collections模块

```python
from collections import Counter
def e():
    '''常用的类
    namedtuple: 接受类型的名称和属性列表创建一个类
    deque: 
    Counter: dict的子类, 键是元素, 值是元素的计数, 他的most_common()方法可以获取最高频率的元素
    OrderDict: dict的子类, 记录键值对插入的顺序
    defaultdict: 类似字典类型, 但可以通过默认的工行函数获得键对应的默认值
    '''
    words = [
        'apple', 'bag', 'cat', 'dog', 'elephant', 'flag', 'glass', 'happy', 'italy',
        'jack', 'cat', 'lens'
    ]
    counter = Counter(words)
    # 获取前三个最高频率的元素
    print(counter.most_common(3))
```

### 数据结构和算法

算法: 解决问题的方法和步骤

评价算法好坏: 渐进时间复杂度和渐进空间复杂度

渐进时间复杂度的大O标记:

#### 简单选择排序

外循环: 列表的元素长度
内循环: 

```python
def select_sort(items, comp=lambda x, y: x < y):
    '''简单选择排序'''
    # 复制新列表
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items
```

#### 穷举法

暴力破解法, 对所有可能验证

> 1. 公鸡5元一只, 母鸡3元一只, 小鸡1元三只.
>    用100元买100只鸡, 公鸡/母鸡/小鸡 各多少只
> 2. A, B, C, D, E 五人分鱼, A将鱼分成五份, 扔掉多余的一条, 拿走自己的一份
>    B将鱼分为5份, 扔掉多余的一条, 拿走自己的一份, C/D/E 也按照同样的方式,
>    他们至少抓了多少鱼

```python

def exhaustive_a():
    '''穷举法'''
    for x in range(20):
        for y in range(33):
            z = 100 - x - y
            if x * 5 + y * 3 + z//3 == 100 and z % 3 == 0:
                print('%s公鸡, %s母鸡, %s小鸡' % (x, y, z))


def exhaustive_b():
    fish = 6
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 5
```

#### 贪婪法

总是做出在当前看来最好的选择, 不追求最优, 快速找到满意解

> 假设小偷有一个背包, 可以装30公斤赃物
>
> | 名称   | 价格 | 重量 |
> | ------ | ---- | ---- |
> | 电脑   | 200  | 20   |
> | 收音机 | 20   | 4    |
> | 表     | 175  | 10   |
> | 花瓶   | 50   | 2    |
> | 书     | 10   | 1    |
> | 油画   | 90   | 9    |
>

```python
def greedy_a():
    class Thing(object):
        '''物品'''

        def __init__(self, name, price, weight):
            self.name = name
            self.weight = weight
            self.price = price

        @property
        def value(self):
            '''性价比'''
            return self.price / self.weight

    def input_thing():
        name_str, price_str, weight_str = input('名字 价格 重量:').split()
        return name_str, int(price_str), int(weight_str)

    def main():
        max_weight, num_of_things = map(int, input('背包重量容量 可用物品件数:').split())
        all_things = []
        for _ in range(num_of_things):
            all_things.append(Thing(*input_thing()))  # 带*会翻译成元组
        all_things.sort(key=lambda x: x.value, reverse=True)
        total_weight = 0
        total_price = 0
        for thing in all_things:
            if total_weight + thing.weight <= max_weight:
                print(f'小偷拿走了{thing.name} 性价比{thing.value}')
                total_weight += thing.weight
                total_price += thing.price
        print(f'总价值{total_price}元, 重{total_weight}')

    main()
```



#### 分治法

将复杂的问题分成两个或更多相同或相似的子问题, 再把子问题分成更小的子问题, 知道可以直接求解

> [快速排序](https://zh.m.wikipedia.org/zh/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F)

#### 回溯法

试探法, 按选优条件向前搜索, 当到达某一步发现原先选择不优或达不到目标时, 退回一步重新选择

> [骑士巡逻](https://zh.m.wikipedia.org/zh/%E9%A8%8E%E5%A3%AB%E5%B7%A1%E9%82%8F)

#### 动态规划

待求解分解成若干个子问题, 先求解病保存这些子问题的解, 避免产生重复运算

### 函数的使用方式

- 将函数视为一等公民

  - 可以复制给变量
  - 可以作为函数的参数
  - 可以作为函数的返回值

- 高阶函数的用法( `filter`, `map` 以及替代品)

  ```python
  items = list(map(lambda = x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
  items = [x ** 2 for x in range(1, 10) if x % 2]
  ```

- 未知参数, 可变参数, 关键字参数, 命名关键字参数

- 参数的原信息 (代码可读性)

- 匿名函数和内联函数的用法

- 闭包和作用域

  - Python搜索变量的LEGB顺数 (Local >>> Embedded >>> Global >>> Built-in)
  - `global` 和 `nonlocal` 的作用
    `gloabl`: 声明或定义全局变量 (使用现有的全局作用域的变量, 或定义一个变量放到全局作用域)
    `nonlocal`: 声明使用嵌套作用域的变量 (嵌套作用域必须存在该变量)

- 装饰器函数 (使用和取消)

### 面向对象相关

#### 三大支柱: 封装, 继承, 多态

#### 类和类的关系

- is-a: 继承
- has-a: 关联 / 聚合 / 合成
- use-a: 依赖

```python
# 扑克游戏
```

#### 对象的复制 (深辅助/深拷贝/深度克隆和浅复制/浅拷贝/影子克隆)

#### 垃圾回收 / 循环引用 / 弱引用

Python使用了自动化内存管理, 这种管理机制以**引用计数**为基础, 同事也引入了**标记-清除**和**分代收集**两种机制为辅的策略

```c++
typedef struct _object {
  /* 引用计数 */
  int ob_refcnt;
  /* 对象指针 */
  struct _typeobject *ob_type;
} PyObject;
```

```c#
/* 增加引用计数的宏定义 */
#define Py_INCREF(op) ((op)->ob_refcnt++)
/* 减少引用计数的宏定义 */
#define Py_RECREF(op) \ //减少计数
	if (--(op)->ob_refcnt != 0) \
		; \
  else \
    __Py_Dealloc((PyObject *)(op))
```

导致引用计数+1的情况:

- 对象被创建, 例如`a = 23`
- 对象呗引用, 例如`b = a`
- 对象被作为参数, 传入到一个函数中, 例如`fuc(a)`
- 对象作为一个元素, 存储在容器中, 例如`list = [a, b]`

导致引用计数-1的情况:

- 对象的别名被显式销毁, 例如`del a`
- 对象的别名被赋予新对象, 例如`a = 24`
- 一个对象离开作用域, 例如函数f执行完毕时, f函数中的局部变量 (全局不会)
- 对象所在的容器被销毁, 或从容器删除对象

