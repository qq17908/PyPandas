# -*- coding: utf-8 -*-
'''
1、multiprocessing模块就是跨平台版本的多进程模块
'''

from multiprocessing import Process

import os

def run_proc(name):
    print 'Run child process %s(%s)' % (name,os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args = ('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'
    
'''
对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
'''
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name,os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name,(end-start))
    
if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool(15)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    
    print 'Wainting for all subprocesses done..'
    p.close()
    p.join()
    print 'All subprocesses done'
    
    
'''
进程间通信
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
'''    
from multiprocessing import Process,Queue
import os,time,random

def write(q):
    for value in ['A','B','C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value
        
if __name__=='__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    
    pw.start()
    
    pr.start()
    
    pw.join()
    
    pr.terminate()

    
    
    
    
    
    
    
    
    