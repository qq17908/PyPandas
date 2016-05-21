#coding:utf-8

'''
使用sqlAlchemy创建User表映射

tushare

参数说明：

code：股票代码，即6位数字代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
start：开始日期，格式YYYY-MM-DD
end：结束日期，格式YYYY-MM-DD
ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
retry_count：当网络异常后重试次数，默认为3
pause:重试时停顿秒数，默认为0
返回值说明：

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
import time
from sqlalchemy.engine import create_engine
from tushare.stock.trading import get_hist_data
from sqlalchemy.sql.schema import Table, MetaData

class DealData():
    def get_stock_hist_data(self):
        stockCode = '002410'
        stockKtype = 'D'
        stockDate = '2010-05-25'
        stockEnd = '2016-05-19'
        t0 = time.time()
        
        hisdatadf = get_hist_data(stockCode,stockDate,stockEnd)
        hisdatadf['ktype'] = stockKtype
        hisdatadf['code']=stockCode
        hisdatadf['date']=hisdatadf.index
        
        dataList = []
        for index,row in hisdatadf.iterrows():
            dataList.append(row.to_dict())
         
        print "DealData:Total time for" + str(time.time() - t0) + "  secs"
        return dataList
    
if __name__ == '__main__':
    engine = create_engine(r'sqlite:///H:\workspacePy\PythonTech\src\pyTrain\ex1.db', echo=True)
    #engine = create_engine(r'sqlite:///C:\Users\Liang.Lu\workspacepy\PythonTech\src\pyTrain\ex1.db', echo=True)

    
    metadata = MetaData(engine)
    histDataT = Table('ka_stock_hist_data',metadata,autoload=True)
        
    conn = engine.connect()
    hist_data = DealData().get_stock_hist_data()
#   result = conn.execute(histDataT.insert())
    t1 = time.time()
    
    #insert数据
    conn.execute(histDataT.insert(),hist_data)
    print "InsertData:Total time for" + str(time.time() - t1) + "  secs"
    