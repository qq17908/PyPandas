# encoding: utf-8
 
import tushare as ts
import pandas as pd
import numpy as np
 
if __name__ == '__main__':
    #当日历史分笔
    #get_today_ticks(code,retry_count,pause)
    #返回：时间、当前价格、涨跌幅、价格变动、成交金额（元）、买卖类型
    df = ts.get_today_ticks('002410',3,0.001)
    print df.head(100)
    
    