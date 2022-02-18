'''
多线程和多进程
'''

from multiprocessing import Process
from threading import Thread
from os import getpgid

from random import randint
from time import time, sleep

def download_task(name):
    print('开始下载%s' % name)
    _time = randint(0, 3)
    sleep(_time)
    print('下载完成, 耗时%sS' % _time)

def main_single():
    '''单线程下载'''
    start = time()
    downloadList = ['Hxert的秘密', '米米的秘密', 'cyo57的密码', '多线程和多进程']
    for _ in downloadList:
        download_task(_)
    end = time()
    print('总耗时%.2fS' % (end-start))

def main_multi_process():
    '''多进程下载'''
    start = time()
    p1 = Process(target=download_task, args=('Hxert', ))
    p2 = Process(target=download_task, args=('cyo57', ))
    p3 = Process(target=download_task, args=('mimi', ))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    # Process创建进程对象, target传入函数, args传递参数
    # Process对象的start()方法启动进程, join方法等待进程结束
    end = time()
    print('总耗时%.2fS' % (end-start))


counter = 0
def count_task(str):
    global counter
    while counter < 10:
        print(str, end='', flush=True)
        counter += 1
        sleep(0.1)

def main_count_task():
    '''错误示范 实际上会输出A B各10次'''
    Process(target=count_task, args=('A', )).start()
    Process(target=count_task, args=('B', )).start()


def main_multi_thread():
    '''多线程下载'''
    start = time()
    t1 = Thread(target=download_task, args=('Hxert', ))
    t2 = Thread(target=download_task, args=('cyo57', ))
    t3 = Thread(target=download_task, args=('mimi', ))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    # Process创建进程对象, target传入函数, args传递参数
    # Process对象的start()方法启动进程, join方法等待进程结束
    end = time()
    print('总耗时%.2fS' % (end-start))


if __name__ == '__main__':
    #main_single()
    #main_multi_process()
    #main_count_task()
    main_multi_thread()