# encoding: utf-8
 
#from pandas import import Series,DataFrame
import tushare as ts
import pandas as pd
import numpy as np
from pandas.core.index import MultiIndex
 
if __name__ == '__main__':
    #当日历史分笔
    #get_today_ticks(code,retry_count,pause)
    #返回：时间、当前价格、涨跌幅、价格变动、成交金额（元）、买卖类型
    #df = ts.get_today_ticks('002410',3,0.001)
    #print df.head(100)
    
    midx = MultiIndex(levels=[['one','two'],['x','y']],labels=[[1,1,0,0],[1,0,1,0]])
    df = pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8]},index = midx)
    print df.to_panel()