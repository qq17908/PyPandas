# -*- coding: utf-8 -*-
#########################################################
#1、错误处理  try...except...finally...
#2、调试
#3、单元测试
#4、文档测试
#########################################################

#断言
#assert 如果失败则跑错AssertionError
def foo(s):
    n = int(s)
    assert n != 0 ,'n is zero!'
    return 10 / n

def main():
    foo('0')

main()

#logging
#logging不会抛出错误，但会输出文件
#debug，info，warning，error等几个级别
#level=WARNING后debug和info就不起作用
#level=INFO后logging.debug就不起作用。

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n=%d' % n)
print(10/n)

#PDB
#-m pdb err.py  执行后进入调试模式
#l - 查看代码
#n - 单步调试
#p - p 变量名  查看变量
#q - 结束调试
