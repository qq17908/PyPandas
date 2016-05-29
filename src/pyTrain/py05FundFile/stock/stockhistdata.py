# coding:utf-8

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
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.engine import create_engine
from sqlalchemy.sql import bindparam,select
from tushare.stock.trading import get_hist_data

class DealData():
    def table_hist_data(self,metadata):
        return Table('ka_stock_hist_data', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('code', String),
                        Column('ktype', String),
                         
                        Column('date', String),
                        Column('open', String),
                        Column('high', String),
                        Column('close', String),
                        Column('low', String),
                        Column('volume', String),
                        Column('price_change', String),
                        Column('p_change', String),
                        Column('ma5', String),
                        Column('ma10', String),
                        Column('ma20', String),
                        Column('v_ma5', String),
                        Column('v_ma10', String),
                        Column('v_ma20', String),
                        Column('turnover', String)
        )
        
    def get_stock_hist_data(self):
        stockCode = '002410'
        stockKtype = 'D'
        stockDate = '2010-05-25'
        stockEnd = '2016-05-19'
        t0 = time.time()
        
        hisdatadf = get_hist_data(stockCode, stockDate, stockEnd)
        hisdatadf['ktype'] = stockKtype
        hisdatadf['code'] = stockCode
        hisdatadf['date'] = hisdatadf.index
        
        dataList = []
        for index, row in hisdatadf.iterrows():
            dataList.append(row.to_dict())
         
        print "DealData:Total time for" + str(time.time() - t0) + "  secs"
        return dataList
    
if __name__ == '__main__':
    engine = create_engine(r'sqlite:///H:\workspacePy\PythonTech\src\pyTrain\ex1.db', echo=True)
    #engine = create_engine(r'sqlite:///C:\Users\Liang.Lu\workspacepy\PythonTech\src\pyTrain\ex1.db', echo=True)

    metadata = MetaData(engine)
    conn = engine.connect()
    
    #create table 创建数据表
    print "create table 创建数据表"
    for tabs in metadata.sorted_tables:
        print ("tablename:" % tabs.name)
    
    histDataT = Table(DealData().table_hist_data(metadata),metadata,autoload=True)    
    
    #通过tushare.get_stock_hist_data 获取数据集
    hist_data = DealData().get_stock_hist_data()
    
###############插入数据####################
#    #insert数据
    #1、add单条数据
    
    
#    #2、add 多条数据
    t1 = time.time()
    conn.execute(histDataT.insert(),hist_data)
    print "InsertData:Total time for" + str(time.time() - t1) + "  secs"

###############删除数据####################
#    #删除表所有数据
#    r = conn.execute(histDataT.delete())     
    
#    #删除条件数据
#    r = conn.execute(histDataT.delete().where(histDataT.c.code=='002410'))

###############修改数据#####################
    s = histDataT.update().where(histDataT.c.open == 12.55).values(high=13.00)
    r = conn.execute(s)
    print r.rowcount
    
    #一次执行多条记录更新
    s = histDataT.update().where(histDataT.c.open == bindparam('oOpenPrice')).values(high=bindparam('nHighPrice'))
    print s
    u = [{'oOpenPrice':12.55,'nHighPrice':13.50},
         {'oOpenPrice':13.0,'nHighPrice':14.50}
         ]
    r = conn.execute(s,u)
    
   #Multiple Table Updates
    
###############查询数据####################
    #查询全表记录
    s = select([histDataT])
    print s
    #获取一条查询记录
    fetchOne = conn.execute(s).fatchone()
    
    #Operators: ==   !=   >  <
    #and_()  or_()  not_()
    #like
    #orderby() groupby()
    #join()   outerjoin()
    #union() union_all()
    
    