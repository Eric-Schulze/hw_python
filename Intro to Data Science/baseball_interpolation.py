import pandas as pd
import numpy as np
import scipy as sp
from scipy import stats

df = pd.read_csv('Master.csv')
df= df[['height','weight']]

df2 = df.fillna(df.mean()[['height','weight']])
print('Starting Height and Weight Mean:')
print(df.mean()[['height','weight']])
print('Height and Weight Mean After Imputation:')
print(df2.mean()[['height','weight']])
print(df2.iloc[1:25][['height','weight']])
print()

df3 = df.interpolate()
print('Starting Height and Weight Mean:')
print(df.mean()[['height','weight']])
print('Height and Weight Mean After Linear Interpolation:')
print(df3.mean()[['height','weight']])
print(df3.iloc[1:25][['height','weight']])
print()

df4 = df.interpolate(method='polynomial',order=2)
print('Starting Height and Weight Mean:')
print(df.mean()[['height','weight']])
print('Height and Weight Mean After 2nd Degree Polynomial Interpolation:')
print(df4.mean()[['height','weight']])
print(df4.iloc[1:25][['height','weight']])
print()

df5 = df.interpolate(method='polynomial',order=3)
print('Starting Height and Weight Mean:')
print(df.mean()[['height','weight']])
print('Height and Weight Mean After 3rd Degree Polynomial Interpolation:')
print(df5.mean()[['height','weight']])
print(df5.iloc[1:25][['height','weight']])
print()

#-----------------------------------------------------------------------
'''
perform a t-test on two sets of baseball data (left-handed and right-handed players)
null hypothese: there is no difference between the two groups
CSV file: baseball_stats.csv
columns: playername | handedness | avg
With a 95% significance level, if there is no difference between the two groups (thus the null hypotheses holds), output True and the tuple returned by scipy.stats.ttest
If there is a difference, output False with the tuple from scipy.stats.ttest
'''

#read the data file into a dataframe
#split the data into two dataframes for left and right handedness
#perform welches twosample t-test 
#if results[1] <= 0.05:
#       print('False', results)
#else:
#       print('True',results)

stats = pd.read_csv('baseball_stats.csv')
left_df = stats['avg'][stats['handedness'] == 'L']
right_df = stats['avg'][stats['handedness'] == 'R']

twosample_result = sp.stats.ttest_ind(left_df,right_df,equal_var=False)
if twosample_result[1] <= 0.05:
       print('False: ', twosample_result)
else:
       print('True: ',twosample_result)




