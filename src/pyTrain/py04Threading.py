# -*- coding: utf-8 -*-
'''
Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块
'''
import time,threading
from blaze.compute.numba import lock

def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0 
    while n<5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name,n)
        time.sleep(1)
    
    print 'thread %s ended.' % threading.current_thread().name
    
    t = threading.Thread(target = loop,name = 'LoopThread')
    t.start()
    t.join()
     
    print 'thread %s ended...' % threading.current_thread().name
 

if __name__ == '__main__':
    loop()


'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享
'''
'''
Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行
'''
import time,threading

balance = 0

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    

def run_thread(n):
    for i in range(10000):
        #先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,)) 

t1.start()
t2.start()
t1.join()
t2.join()

print balance  
