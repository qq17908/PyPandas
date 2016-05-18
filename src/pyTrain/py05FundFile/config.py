#coding:utf-8

from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.engine import create_engine

class initDatabase():
    def init(self):
        engine = create_engine('sqlite:///ex1.db', echo=True)
        metadata = MetaData();  
        
    def create_hist_data(self):
        histdata = Table('ka_stock_hist_data',self.metadata,
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
    
    def update_hist_data(self):
       pass