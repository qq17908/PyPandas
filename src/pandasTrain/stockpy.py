# encoding: utf-8
 
<<<<<<< HEAD
#from pandas import import Series,DataFrame
import tushare as ts
import pandas as pd
import numpy as np
from pandas.core.index import MultiIndex
from cryptography.hazmat.primitives.ciphers.modes import Mode
 
if __name__ == '__main__':
    #当日历史分笔
    #get_today_ticks(code,retry_count,pause)
    #返回：时间、当前价格、涨跌幅、价格变动、成交金额（元）、买卖类型
    #df = ts.get_today_ticks('002410',3,0.001)
    #print df.head(100)
    
    #历史行情
    #get_hist_data(code,start,end,ktype,retry_count,pause)
    #code:股票代码
    #ktype：数据类型，D=日K线，W=周；M=月；5=5分钟；15=15分钟；30=30分钟；60=60分钟
    #df = ts.get_hist_data('002410')
    df = ts.get_stock_basics()
    date = df.ix['002410']['timeToMarket']
    
    #复权数据
    #get_h_data(code,start,end,autype,index,retry_count,pause)
    #autype:string-复权类型，qfq-前复权；hfq-后复权；None-不复权；默认qfq
    #返回：date、open、high、close、low、volume、amount
    dateStart = '2015-05-25'
    dateEnd = '2016-04-15'
    df = ts.get_h_data('002410',start=dateStart,end=dateEnd,autype='qfq')
    
    df.to_csv('d:/002410.csv',mode='a', header = None)
        
    print 'finish!'
=======
import tushare as ts
import pandas as pd
import numpy as np
 
if __name__ == '__main__':
    #当日历史分笔
    #get_today_ticks(code,retry_count,pause)
    #返回：时间、当前价格、涨跌幅、价格变动、成交金额（元）、买卖类型
    df = ts.get_today_ticks('002410',3,0.001)
    print df.head(100)
    
>>>>>>> refs/remotes/origin/master
    