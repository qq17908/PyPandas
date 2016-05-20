# -*- coding: utf-8 -*-

import tushare as ts
import pandas as pd
import numpy as np

def list_all_dict(dict_a):
    if isinstance(dict_a,dict):
        for x in range(len(dict_a)):
            temp_key = dict_a.keys()[x]
            temp_value = dict_a[temp_key]
            print "%s:%s" % (temp_key,temp_value)
            list_all_dict(temp_value)

hisdatadf = ts.get_hist_data('002410','2016-05-17','2016-05-18')
hisdatadf['ktype'] = 'D'
hisdatadf['code']='002410'

#l = [{"code":item["code"],"ktype":item["ktype"]}for item in hisdatadf]
row = next(hisdatadf.iterrows())[1]
row

tmphisdataUnit1 = hisdatadf.iloc[0].to_dict()
tmphisdataUnit2 = hisdatadf.iloc[1].to_dict()
l = [tmphisdataUnit1,tmphisdataUnit2]

tmplist = ['tmphisdataUnit1']
tmplist.append('tmphisdataUnit2')





