#coding:utf-8
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from pyTrain.py05FundFile.table_Hist_Data import Hist_data_table



engine = create_engine(r'sqlite:///C:\Users\Liang.Lu\workspacepy\PythonTech\src\pyTrain\ex1.db', echo=True)
DBsession = sessionmaker(bind=engine)
session = DBsession()


query = session.query(Hist_data_table)
print query.count()