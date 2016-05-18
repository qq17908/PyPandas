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
from sqlalchemy.sql.elements import or_, not_
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.sqltypes import DECIMAL
import sqlalchemy

Base = declarative_base()

print sqlalchemy.__version__
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

#user = session.query(User).filter(User.id=='4').one()

print '#############################'
query = session.query(User)
print query
print query.statement
print query.first().name
print query.filter(User.id == 2).first().name
print query.get(2).name
print query.filter('id=2').first().name

print '#############################'
query2 = session.query(User.name)
print query2.all()
print query2.limit(1).all() #最多返回1条记录
print query2.offset(1).all() #从第2条记录开始返回
print query2.order_by(User.name).all()
print query2.order_by('name').all()
print query2.order_by(User.name.desc()).all()
print query2.order_by('name desc').all()
print session.query(User.id).order_by(User.name.desc(),User.id).all()

print query2.filter(User.id == 1).scalar() # 如果有记录，返回第一条记录的第一个元素
print session.query('id').select_from(User).filter('id = 1').scalar()
print query2.filter(User.id > 1, User.name != 'a').scalar() # and

query3 = query2.filter(User.id > 1) # 多次拼接的 filter 也是 and
query3 = query3.filter(User.name != 'a')
print query3.scalar()
print query2.filter(or_(User.id == 1, User.id == 2)).all() # or
print query2.filter(User.id.in_((1, 2))).all() # in

print '#############################'
query4 = session.query(User.id)
print query4.filter(User.name == None).scalar()
print query4.filter('name is null').scalar()
print query4.filter(not_(User.name == None)).all() # not
print query4.filter(User.name != None).all()

print query4.count()
print session.query(func.count('*')).select_from(User).scalar()
print session.query(func.count('1')).select_from(User).scalar()
print session.query(func.count(User.id)).scalar()
print session.query(func.count('*')).filter(User.id > 0).scalar() # filter() 中包含 User，因此不需要指定表
print session.query(func.count('*')).filter(User.name == 'a').limit(1).scalar() == 1 # 可以用 limit() 限制 count() 的返回数
print session.query(func.sum(User.id)).scalar()
print session.query(func.now()).scalar() # func 后可以跟任意函数名，只要该数据库支持
print session.query(func.current_timestamp()).scalar()
print session.query(func.md5(User.name)).filter(User.id == 1).scalar()

query.filter(User.id == 1).update({User.name: 'c'})
user = query.get(1)
print user.name

print '#############################'
user.name = 'd'
session.flush() # 写数据库，但并不提交
print query.get(1).name

session.delete(user)
session.flush()
print query.get(1)

session.rollback()
print query.get(1).name
query.filter(User.id == 1).delete()
session.commit()
print query.get(1)


print '########如何连接表？########'
# print session.query(User.id).join(Friendship, User.id == Friendship.user_id1).all() # 所有有朋友的用户
# print session.query(distinct(User.id)).join(Friendship, User.id == Friendship.user_id1).all() # 所有有朋友的用户（去掉重复的）
# print session.query(User.id).join(Friendship, User.id == Friendship.user_id1).distinct().all() # 同上
# print session.query(Friendship.user_id2).join(User, User.id == Friendship.user_id1).order_by(Friendship.user_id2).distinct().all() # 所有被别人当成朋友的用户
# print session.query(Friendship.user_id2).select_from(User).join(Friendship, User.id == Friendship.user_id1).order_by(Friendship.user_id2).distinct().all() # 同上，join 的方向相反，但因为不是 STRAIGHT_JOIN，所以 MySQL 可以自己选择顺序
# print session.query(User.id, Friendship.user_id2).join(Friendship, User.id == Friendship.user_id1).all() # 用户及其朋友
# print session.query(User.id, Friendship.user_id2).join(Friendship, User.id == Friendship.user_id1).filter(User.id < 10).all() # id 小于 10 的用户及其朋友
# print session.query(User.id, Friend.id).join(Friendship, User.id == Friendship.user_id1).join(Friend, Friend.id == Friendship.user_id2).all() # 两次 join，由于使用到相同的表，因此需要别名
# print session.query(User.id, Friendship.user_id2).outerjoin(Friendship, User.id == Friendship.user_id1).all() # 用户及其朋友（无朋友则为 None，使用左连接）


print '#####如何正确使用事务？#####'
#如果被查询的字段没有加索引的话，就会变成锁整张表了
# money = Column(DECIMAL(10, 2), index=True)
# user1 = session2.query(User).with_lockmode('update').get(1)

# print('type:',type(user))
# print('name:',user.name)
session.close()

####################


