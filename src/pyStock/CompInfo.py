#coding=utf-8

import tushare as ts
import sys

reload(sys)
#sys.setdefaultencoding()
print sys.getdefaultencoding()
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
reload(sys)

df=ts.get_stock_basics()

df.to_excel('d:/Desktop/2015.xlsx')
print 'finish!'