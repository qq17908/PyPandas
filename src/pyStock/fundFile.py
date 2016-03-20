#coding:utf-8

import pandas as pd
import numpy as np
import tushare as ts
import os
import time

class FundInfos():
    def __init__(self):
        print "_init_"
        
if __name__ == "__main__":
    #读取CSV文件
    filePath = 'd:\Desktop\stock.csv'
    stock_df = pd.read_csv(filePath,header=0,names = ['code','gPrice','gNumber','gDate'],dtype={'code':object,'gDate':np.object})
    
    stock_realtime_df = ts.get_realtime_quotes(['002410','600118','600748','601989','600176'])
    
    stock_realtime_df = stock_realtime_df[['code','name','open','price']]
    
    stock_infos_df = stock_realtime_df.merge(stock_df,how='outer').fillna({'gPrice':0,'gNumber':0,'gDate':'0000/00/00'})

    #购买总价
    stock_TotalPrice = pd.Series(stock_infos_df['gPrice'] * stock_infos_df['gNumber'].astype(np.float64),name='gTPrice')

    #盈亏金额
    stock_ProfileLoss_Price = pd.Series((stock_infos_df['price'].astype(np.float64) - stock_infos_df['gPrice']) * stock_infos_df['gNumber'].astype(np.float64),name='gTProfileLoss')
    
    #盈亏比
    stock_ProfileLoss_Percent = pd.Series((stock_ProfileLoss_Price / stock_TotalPrice) * 100,name = 'gProfileLossPercent')
    
    #拼接数据
    stock_infos_df = pd.concat([stock_infos_df,stock_TotalPrice],axis=1)
    stock_infos_df = pd.concat([stock_infos_df,stock_ProfileLoss_Price],axis=1)
    stock_infos_df = pd.concat([stock_infos_df,stock_ProfileLoss_Percent],axis=1)
    print stock_infos_df
    
    #系统每隔3秒刷新数据
    time.sleep(5)
    #清除屏幕数据，准备显示新数据
    os.system('cls') 
    #print stock_infos_df