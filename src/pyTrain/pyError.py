# -*- coding: utf-8 -*-
#########################################################
#1、错误处理  try...except...finally...
#2、调试
#3、单元测试
#4、文档测试
#########################################################


class tryClass():
    def test():
    #try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕
        try:
            print('try')
            r = 10/0
            print ('result',r)
        except ZeroDivisionError as e:
            print('except:',e)
        finally:
            print('finally....')
        
        print('END')
        
    #多个except来捕获不同类型的错误
    def test2():
        try:
            print('try')
            r = 10/int('a')
            print ('result',r)
        except ValueError as e:
            print('ValueError:',e)
        except ZeroDivisionError as e:
            print('except:',e)
        finally:
            print('finally....')
        
        print('END')
        
    
    #except语句后加个else，当没有错误发生时，会自动执行else语句
    def test3():
        try:
            print('try')
            r = 10/int('2')
            print ('result',r)
        except ValueError as e:
            print('ValueError:',e)
        except ZeroDivisionError as e:
            print('except:',e)
        else:
            print ('no error')
        finally:
            print('finally....')
        
        print('END')

#Python内置的logging模块可以非常容易地记录错误信息
#通过配置，logging还可以把错误记录到日志文件里
class errloggClass():
    import logging
    
    def foo(s):
        return 10/int(s)
    
    def bar(s):
        return foo(s)*2
    
    def main():
        try:
            bar('0')
        except Exception as e:
            logging.exception(e)
            
    main()
    print('END')
    

#抛出错误
#如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
class errRaiseClass():
    pass

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0 :
       raise FooError('invalid value:%s' % s)
    return 10/n
    
foo('0')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        