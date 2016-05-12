
import pandas as pd
import numpy as np

if __name__ == '__main__':
    data1 = pd.DataFrame(np.ones((6,3),dtype = float),
                      columns=['a','b','c'],
                      index=pd.date_range('6/12/2012',periods=6))
    
    data2 = pd.DataFrame(np.ones((6,3),dtype=float)*2,
                      columns=['a','b','c'],
                      index = pd.date_range('6/13/2012',periods=6)
                      )
    spliced = pd.concat([data1.ix[:'2012-06-14'],data2.ix['2012-06-15':]])
    print spliced
    