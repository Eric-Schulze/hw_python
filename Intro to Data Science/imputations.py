import pandas as pd
import numpy as np
import scipy as sp

# 1. reindexing : to get missing data
df = pd.DataFrame(np.random.randn(5,3), index=['a','c','e','f','h'],columns=['one','two','three'])
print(df)
print()

df2 = df.reindex(['a','b','c','d','e','f','g','h'])

print(df2)
print()

print(pd.isnull(df2['one'])) #detect missing values
print()

print(df2['two'].notnull())
print()

#replace missing values with some scalar
df2 = df2.fillna(0) #fill NaN with 0
print(df2)
print()

dff = pd.DataFrame(np.random.randn(10,3),columns = list('ABC'))
print(dff)
print()

#fill diff with NaNs
dff.iloc[3:5, 0] = np.nan
dff.iloc[4:6, 1] = np.nan
dff.iloc[5:8, 2] = np.nan
print(dff)
print()

dff1 = dff.fillna(dff.mean()) #individual column mean
print(dff1)
print()

#restrict to certain columns
dff2 = dff.fillna(dff.mean()['B':'C'])
print(dff2)
print()

'''
Linear Interpolation
1   2.1
2   NaN
3   4.7
Missing value for 2 is going to be (2.1 + 4.7)/ 2.0
'''

df3 = pd.DataFrame({'A' : [1,2.1,np.nan,4.7,5.6,6.8],
                                  'B' : [0.25, np.nan, np.nan, 4, 12.2, 14.4]})
print(df3)
print()
df3 = df3.interpolate()
print(df3)
print()


df4 = pd.DataFrame({'A' : [1,2.1,np.nan,4.7,5.6,6.8],
                                  'B' : [0.25, np.nan, np.nan, 4, 12.2, 14.4]})
print(df4)
print()
df4 = df4.interpolate(method='polynomial',order=2)
print(df4)
print()

