#coding:utf-8
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Integer

Base = declarative_base()
dbname =r'sqlite:///C:\Users\Liang.Lu\workspacepy\PythonTech\src\pyTrain\ex1.db'
#dbname =r'sqlite:///H:\workspacePy\PythonTech\src\pyTrain\ex1.db'
engine = None

def init_sqlalchemy(dbname):
    global engine
    engine = create_engine(dbname, echo=False)
    DBsession = sessionmaker()
    DBsession.configure(bind=engine, autoflush=False, expire_on_commit=False)
#   Base.metadata.drop_all(engine)
#   Base.metadata.create_all(engine)

    
#histData = Hist_data_table(code='002410',ktype='D',date='2016-05-18',open='13.00',high='13.05',close='12.45',low='12.38',volume='137127.11',price_change='-0.68',p_change='-5.18',ma5='13.142',ma10='13.390',ma20='13.282',v_ma5='98529.77',v_ma10='113193.34',v_ma20='113489.80',turnover = '1.58')

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