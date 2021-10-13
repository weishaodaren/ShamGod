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
    p1 = Process(target=download_task, args=('Python.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('Toyko.avi',))
    p2.start()
    p1.join() # 等待执行结束
    p2.join()
    end = time()
    print('一共耗时%2f秒' % (end - start))

if __name__ == '__main__':
    main()
    
