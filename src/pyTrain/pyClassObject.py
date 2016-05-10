##coding=utf-8
####################pyClassObject.py####################
#1、类和实例
#2、访问限制
#3、继承和多态
#4、获取对象信息
#5、实例属性和类属性
###############################
#1、__slots__
#2、@property
#3、多重继承
#MixIn目的给一个类增加多个功能，而不是设计多层次的复杂的继承关系
#4、定制类
#5、使用枚举类 
#6、使用元类  
#   关键字：metaclass
#   先定义metaclass，再定义类class，在此间实例
########################################################


##类@property
class Student(object):
    @property
    def score(self):
      return  self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        if value <0 or value>100:
            raise ValueError('score must between 0~100')
        self._score = value

stu = Student()
stu.score = 10
print stu.score


