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

from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy  import Column,Integer,String
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()
class Hist_data_table(Base):
    __tablename__ = 'ka_stock_hist_data'
    
    id = Column(Integer,primary_key = True)
    code = Column(String)
    ktype = Column(String)
    date = Column(String)
    open = Column(String)
    high = Column(String)
    close = Column(String)
    low = Column(String)
    volume = Column(String)
    price_change = Column(String)
    p_change = Column(String)
    ma5 = Column(String)
    ma10 = Column(String)
    ma20 = Column(String)
    v_ma5 = Column(String)
    v_ma10 = Column(String)
    v_ma20 = Column(String)
    turnover = Column(String)
    
class SQLExecute():
    def insertData(self):
        histData = Hist_data_table(code='002410',ktype='D',date='2016-05-18',open='13.00',high='13.05',close='12.45',low='12.38',volume='137127.11',price_change='-0.68',p_change='-5.18',ma5='13.142',ma10='13.390',ma20='13.282',v_ma5='98529.77',v_ma10='113193.34',v_ma20='113489.80',turnover = '1.58')
        
    def selectData(self):
        pass
    def delData(self):
        pass
    def updateData(self):
        pass

if __name__ == '__main__':
    engine = create_engine(r'sqlite:///H:\workspacePy\PythonTech\src\pyTrain\ex1.db', echo=True)
    #engine = create_engine(r'sqlite:///C:\Users\Liang.Lu\workspacepy\PythonTech\src\pyTrain\ex1.db', echo=True)
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    #histData = Hist_data_table(code='002410',ktype='D',date='2016-05-18',open='13.00',high='13.05',close='12.45',low='12.38',volume='137127.11',price_change='-0.68',p_change='-5.18',ma5='13.142',ma10='13.390',ma20='13.282',v_ma5='98529.77',v_ma10='113193.34',v_ma20='113489.80',turnover = '1.58')
    #session.add(histData)
    #session.commit()
    query = session.query(Hist_data_table)
    for row in session.query(Hist_data_table,Hist_data_table.code).all():
        print(row.Hist_data_table,row.code)
    
    
    