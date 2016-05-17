# -*- coding: utf-8 -*-
import sqlite3

# conn = sqlite3.connect('ex1.db')
# cursor = conn.cursor()
# cursor.execute('select * from user')
# values = cursor.fetchall()
# print values
# 
# cursor.close()
# conn.close()

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__='user'
    
    id = Column(String(20),primary_key=True)
    name = Column(String(20))


#初始化数据库链接
engine = create_engine('sqlite:///ex1.db')

#创建DBsession类型
DBsession = sessionmaker(bind=engine)

'''
#创建Session对象
session = DBsession()
#创建新User对象
new_user = User(id='4',name='Paul4')
#添加到Session
session.add(new_user)
#提交保存到数据库
session.commit()
#关闭Session
session.close()
'''

####################
session = DBsession()
user = session.query(User).filter(User.id=='4').one()
print('type:',type(user))
print('name:',user.name)
session.close()

