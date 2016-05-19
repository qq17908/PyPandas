#coding:utf-8
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative.api import declarative_base

Base = declarative_base()
dbname =r'sqlite:///C:\Users\Liang.Lu\workspacepy\PythonTech\src\pyTrain\ex1.db'
engine = None

def init_sqlalchemy(dbname):
    global engine
    engine = create_engine(dbname, echo=False)
    DBsession = sessionmaker()
    DBsession.configure(bind=engine, autoflush=False, expire_on_commit=False)
#   Base.metadata.drop_all(engine)
#   Base.metadata.create_all(engine)

