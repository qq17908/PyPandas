# -*- coding: utf-8 -*-

import tushare as ts
import pandas as pd
import numpy as np

########对Pandas数据进行遍历##############################
def _map(data,exp):
    for index,row in data.iterrows():
        for col_name in data.columns:
            row[col_name] = exp(row[col_name])
    return data

def _1map(data,exp):
    _data = [[exp(row[col_name])
        for col_name in data.columns]
        for index,row in data.iterrows()
    ]
    return _data

inp = [{'c1':10, 'c2':100}, {'c1':11,'c2':110}, {'c1':12,'c2':120}]
df = pd.DataFrame(inp)
temp = _map(df, lambda ele: ele+1 )
print temp

_temp = _1map(df, lambda ele: ele+1)
res_data = pd.DataFrame(_temp)         # 对2级list转换成DataFrame
print res_data

'''end'''
###############################################################################
#遍历dict
def list_all_dict(dict_a):
    if isinstance(dict_a,dict):
        for x in range(len(dict_a)):
            temp_key = dict_a.keys()[x]
            temp_value = dict_a[temp_key]
            print "%s:%s" % (temp_key,temp_value)
            list_all_dict(temp_value)
''''''
stockCode = '002410'
stockKtype = 'D'
stockDate = '2016-05-17'
stockEnd = '2016-05-18'
hisdatadf = ts.get_hist_data(stockCode,stockDate,stockEnd)
hisdatadf['ktype'] = stockKtype
hisdatadf['code']=stockCode
hisdatadf['date']=hisdatadf.index

#l = [{"code":item["code"],"ktype":item["ktype"]}for item in hisdatadf]
#l = [l.append(item.to_dict()) for index,item in hisdatadf.iterrows()]
#print l
l = []
for index,row in hisdatadf.iterrows():
    l.append(row.to_dict())


tmphisdataUnit1 = hisdatadf.iloc[0].to_dict()
tmphisdataUnit2 = hisdatadf.iloc[1].to_dict()
l = [tmphisdataUnit1,tmphisdataUnit2]

tmplist = ['tmphisdataUnit1']
tmplist.append('tmphisdataUnit2')





