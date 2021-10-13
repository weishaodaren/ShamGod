from multiprocessing import Process
from time import sleep

counter = 0

def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='\n', flush=True)
        counter += 1
        sleep(.01)

def main():
    Process(target=sub_task, args=('Ping' ,)).start()
    Process(target=sub_task, args=('Pong' ,)).start()

if __name__ == '__main__':
    main()