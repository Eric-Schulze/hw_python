import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats

#generate random data from normal distribution
#sample 50 data points with mean = 0 and variance  = 1

data1 = np.random.normal(0,1,size=50) #mean,std dev, size
data2 = np.random.normal(2,1,size=50)

print(data1)
print()
print(data2)
print()

#One sample test
#the null hypotheses is that the mean m of the sample is equal to the true mean of the population (i.e. there is 0 difference between the two means)
#hence m == mean, 95% confidence

onesample_result = sp.stats.ttest_1samp(data1,0) #0 is the null hypotheses say the difference between two means is 0

print(onesample_result)
print()

'''
We have two independently sampled datasets with equal variance and we are interested to know if m1 and m2 are identical
'''
twosample_result = sp.stats.ttest_ind(data1,data2,equal_var=False)
print(twosample_result)
print()

#if p-value < statistics, reject the null hypotheses

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
left_df = stats



