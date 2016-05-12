# -*- coding: utf-8 -*-

class Dict(dict):
    '''
    #当函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值
    '''
    def __init__(self,**kw):
        super().__init__(**kw)
    
    def __getattr__(self,key):
        try:
            return self(key)
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute %s'" %key)
    
    def __setattr__(self,key,value):
        self[key] = value


'''
对函数abs()，我们可以编写出以下几个测试用例：
输入正数，比如1、1.2、0.99，期待返回值与输入相同；
输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
输入0，期待返回0；
输入非数值类型，比如None、[]、{}，期待抛出TypeError。
'''

import unittest
#from mydict import Dict
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
        
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')
    
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')
    
    def test_keyerror(self):
        d  = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
            
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
            
    #setUp()和tearDown()方法会分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print('setUp...')
    
    def tearDown(self):
        print('tearDown...')

if __name__ =="__main__":
    unittest.main()