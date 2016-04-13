#coding=utf-8

import tushare as ts
import os
import time

#通过tushare中获取：
#1、历史行情数据
#2、复权历史数据
#3、实时行情数据
#4、大盘指数
#5、实时分笔
#6、历史分笔数据
#7、当日历史分笔
#
class StockInfos():
    def __init__(self):
        print "_init_"
        
    #历史行情数据、复权历史数据、实时行情数据、大盘指数、实时分笔、个股历史分笔数据、当日历史分笔
    def getStock(self):
        print "GetStock!!!"
    
    ##实时分笔
    def get_realtime_quotes_single(self):
        print "get_realtime_quotes_single"
        
    def get_realtime_quotes_much(self):
        print "get_realtime_quotes_much"
    
if __name__ =="__main__":
#    StockInfos si
    while True:
        print time.strftime('%Y-%m-%d %X',time.localtime())
        df = ts.get_realtime_quotes(['002410','600118','600748','601989','600176']) #Single stock symbol
        dfResult=df[['code','name','price','bid','ask','volume','amount','time']]
    
        #定义数据输出：股票代码、股票名称、开盘价等
        print dfResult
        
        #系统每隔3秒刷新数据
        
        time.sleep(5)
        #清除屏幕数据，准备显示新数据
        os.system('cls') 
        
    print('done!')