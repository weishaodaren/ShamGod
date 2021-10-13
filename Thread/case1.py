from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
     print('开始下载%s' % filename)
     download_time = randint(5, 10)
     sleep(download_time)
     print('%s下载完成！耗时%d秒' % (filename, download_time))


def main():
    start = time()
    t1 = Thread(target=download, args=('P.pdf', ))
    t1.start()
    t2 = Thread(target=download, args=('A.mp4', ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('一共耗时%.3f' % (end - start))


if __name__  == '__main__':
    main()