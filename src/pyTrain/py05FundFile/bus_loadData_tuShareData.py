#coding:utf-8
from pyTrain.py05FundFile.table_Hist_Data import Hist_data_table
from tushare.stock.trading import get_hist_data

class TuShareData:
    '''
        get_hist_data(code,start,end,ktype,retry_count,pause)
        参数：
            ktype：数据类型，D=日K线，W=周；M=月；5=5分钟；15=15分钟；30=30分钟；60=60分钟
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
            
        返回：
            date：日期
            open：开盘价
            high：最高价
            close：收盘价
            low：最低价
            volume：成交量
            price_change：价格变动
            p_change：涨跌幅
            ma5：5日均价
            ma10：10日均价
            ma20:20日均价
            v_ma5:5日均量
            v_ma10:10日均量
            v_ma20:20日均量
            turnover:换手率[注：指数无此项]
    '''
    def get_stock_hist_data(self):
        df = get_hist_data('002410','2016-05-17','2016-05-18')


if __name__ == '__main__':
    histData = TuShareData().get_stock_hist_data()
    
    print histData