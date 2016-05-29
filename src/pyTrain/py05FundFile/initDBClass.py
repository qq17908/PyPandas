#coding:utf-8

from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.engine import create_engine

class initDatabase():
    def __init__(self):
        #self._engine = create_engine(r'sqlite:///C:\Users\Liang.Lu\workspacepy\PythonTech\src\pyTrain\ex1.db', echo=True)
        self._engine= create_engine(r'sqlite:///H:\workspacePy\PythonTech\src\pyTrain\ex1.db', echo=True)
        self._metadata = MetaData(self._engine);  
        
    def create_hist_data(self):
        histData = Table('ka_stock_hist_data',self._metadata,
                         Column('id',Integer,primary_key=True),
                         Column('code',String),
                         Column('ktype',String),
                         
                         Column('date',String),
                         Column('open',String),
                         Column('high',String),
                         Column('close',String),
                         Column('low',String),
                         Column('volume',String),
                         Column('price_change',String),
                         Column('p_change',String),
                         Column('ma5',String),
                         Column('ma10',String),
                         Column('ma20',String),
                         Column('v_ma5',String),
                         Column('v_ma10',String),
                         Column('v_ma20',String),
                         Column('turnover',String)
                         )
        
        histData.create()
    
    def update_hist_data(self):
       pass
   
if __name__ == '__main__':
    initDatabase().create_hist_data()
