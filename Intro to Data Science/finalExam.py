import numpy as np
import scipy as sp
from scipy import stats
import pandas as pd
import pandasql as pds
import sqlite3 as sl3
from sklearn import cluster, datasets
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

#Question #1: Impute 'NR' as 0
df = pd.read_csv('APData.csv')

print('Question #1: Impute "NR" as 0')
print(df)

df1 = df.apply(lambda x: x.astype(str).str.lower())
df1 = df1.applymap(lambda x: x.replace('nr',''))
df1['2a'] = pd.to_numeric(df1['2a'])
df1['2b'] = pd.to_numeric(df1['2b'])
df1['2c'] = pd.to_numeric(df1['2c'])
df1['2d'] = pd.to_numeric(df1['2d'])
df1['ID'] = pd.to_numeric(df1['ID'])
df1['Decision'] = pd.to_numeric(df1['Decision'])

df2 = df1.fillna(0)
print('After Imputation:')
print(df2)
print()

#Question #2: Simple Statistics
df3 = pd.DataFrame({'2a':pd.Series([np.mean(df2['2a']), np.median(df2['2a']), np.std(df2['2a'])], index=['MEAN', 'MEDIAN', 'STD DEV']),
           '2b':pd.Series([np.mean(df2['2b']), np.median(df2['2b']), np.std(df2['2b'])], index=['MEAN', 'MEDIAN', 'STD DEV']),
           '2c':pd.Series([np.mean(df2['2c']), np.median(df2['2c']), np.std(df2['2c'])], index=['MEAN', 'MEDIAN', 'STD DEV']),
           '2d':pd.Series([np.mean(df2['2d']), np.median(df2['2d']), np.std(df2['2d'])], index=['MEAN', 'MEDIAN', 'STD DEV'])})
           
print('Question #2: Simple Statistics')
print(df3)
print()

#Question #3: SQL Queries
print('Question #3: SQL Queries')
con = sl3.connect('final.db')
cur = con.cursor()
df4 = df2.copy()
df4.rename(columns=lambda x: x.replace('2','two_').lower(), inplace=True)
df4.to_sql("questionscores", con, if_exists="replace")

cur.execute("select Language from questionscores Group By Language Having Count(*) = (Select Max(count) From (Select Count(*) as count from questionscores Group By Language) tmp)")
mostPopLang = cur.fetchall()

print('Most Popular Language: ' + str(mostPopLang))
print()

cur.execute("select Language from questionscores Group By Language Having Count(*) = (Select Min(count) From (Select Count(*) as count from questionscores Group By Language) tmp)")
leastPopLang = cur.fetchall()

print('Least Popular Languages: ' + str(leastPopLang))
print()

cur.execute("create table avg_scores(question text, average float)")
con.commit()

cur.execute("insert into avg_scores values('2a', (select avg(two_a) from questionscores))")
con.commit()
cur.execute("insert into avg_scores values('2b', (select avg(two_b) from questionscores))")
con.commit()
cur.execute("insert into avg_scores values('2c', (select avg(two_c) from questionscores))")
con.commit()
cur.execute("insert into avg_scores values('2d', (select avg(two_d) from questionscores))")
con.commit()

cur.execute("select question from avg_scores where average = (select Min(average) from avg_scores)")
mostDiffQuest = cur.fetchall()

print('Most Difficult Question: ' + str(mostDiffQuest))
print()

cur.execute("select question from avg_scores where average = (select Max(average) from avg_scores)")
leastDiffQuest = cur.fetchall()

print('Least Difficult Question: ' + str(leastDiffQuest))
print()

cur.execute("select ID from questionscores where two_c < 2")
idsLessThan2 = cur.fetchall()

print('IDs for Score < 2 on Question 2c: ' + str(idsLessThan2))
print()

cur.execute("select ID from questionscores where two_d < (select AVG(two_d) from questionscores)")
idsLessThanMean = cur.fetchall()

print('IDs for Score < Mean for Question 2d: ' + str(idsLessThanMean))
print()


cur.execute("drop table avg_scores")
con.commit()
con.close()

#Question #4: Is the data Normally Distributed? Histograms for 2c and 2d
df5 = df2[['2c', '2d']]
df5.plot.hist(bins=20,alpha=0.5)
plt.show()

print('Question #4: Is the data Normally Distributed? Histograms for 2c and 2d')
print('No, the data is not normally distributed')
print()


#Question #5: One-Sample T-Test on 2c and 2d
onesample_result_2c = sp.stats.ttest_1samp(df2['2c'],0) 
onesample_result_2d = sp.stats.ttest_1samp(df2['2d'],0) 

print('Question #5: One-Sample T-Test on 2c and 2d')
print('2c: ' + str(onesample_result_2c))
print('2d: ' + str(onesample_result_2d))
print()

#Question #6: Linear Regression with Gradient Descent using 2b, 2c, and 2d
def compute_cost(features, values, theta):
    m = len(values) #number of data points
    sum_of_square_errors = np.square(np.dot(features,theta) - values).sum()
    cost = sum_of_square_errors / (2 * m)
    return cost
    
    
#use small value for alpha, around 0.1
def gradient_descent(features, values, theta, alpha, num_iterations):
    m = len(values) #number of data points
    cost_history = []
    for i in range(num_iterations):
        predicted_values = np.dot(features,theta)
        theta = theta - ( alpha / m ) * np.dot(features.T,(predicted_values - values))
        cost = compute_cost(features, values, theta)
        cost_history.append(cost)
    return theta, pd.Series(cost_history)
    
features = df2[['2b','2c', '2d']]

theta = [[0.3],[0.4],[0.3]]

values = df2[['Decision']]

alpha = 0.1
num_iterations = 100
prediction_theta, cost_history = gradient_descent(features,values,theta,alpha,num_iterations)

print('Question #6: Linear Regression with Gradient Descent using 2b, 2c, and 2d')
print('Alpha: ' + str(alpha))
print('Number of Iterations:' + str(num_iterations))
print('Original Theta: ' + str(theta))
print('Prediction Theta: ' + str(prediction_theta))
print()

#Question #7: R^2 of Coeffiencts from #6
def r_squared(predictions, values):
    sst = ((values - np.mean(values))**2).sum()
    ssr = ((predictions - values)**2).sum()
    r_sq = 1 - ssr / sst
    return r_sq
    
predictions = np.dot(features, prediction_theta)
r_sq = r_squared(predictions, values)

print('Question #7: R^2 of Coeffiencts from #6')
print('R-Squared: ' + str(r_sq))
print()

#Question #8: K-Means Clustering using 2b, 2c, and 2d with K=5
print('Question #8: K-Means Clustering using 2b, 2c, and 2d with K=5')
df6 = df2[['2b', '2c', '2d']]
k_means = cluster.KMeans(n_clusters = 5)

k_means.fit(df6)
df6 = df6.assign(label=k_means.labels_)
df6 = df6.assign(id=df2['ID'])

df6_sorted = df6.sort_values(['label'])

current_label = 'A'
for index, row in df6_sorted.iterrows():
    if row['label'] != current_label:
        print()
        current_label = row['label']
        print('IDs in Group ' + str(current_label))
    s = str(row['id'])
    print(s.rstrip('0').rstrip('.') if '.' in s else s)
    
print()

#Question #9: Is there a bias towards a language?
df7 = df2.copy()
df7['Avg'] = np.nan
for index, row in df7.iterrows():
    df7.iloc[index,-1] = (row['2a'] + row['2b'] + row['2c'] + row['2d']) / 4.0
    
accepted_scores = df7[['2a','2b','2c','2d','Language','Avg']][df7['Decision'] == 1]
rejected_scores = df7[['2a','2b','2c','2d','Language','Avg']][df7['Decision'] == 0]

accepted_scores_grouped = accepted_scores.groupby('Language').mean()
rejected_scores_grouped = rejected_scores.groupby('Language').mean()

print('Question #9: Is there a bias towards a language?')
print()
print('Averages Scores for Students Whose Programs were Accepted')
print(accepted_scores_grouped)
print()
print('Averages Scores for Students Whose Programs were Rejected')
print(rejected_scores_grouped)
print()
print('It is hard to define patterns with such a small dataset, but putting that aside and assuming that the grader' +
        ' was the same person for all the scores, it can be seen that programs written in Alice and Lua were graded harder, ' + 
        'because the only people to have their programs accepted had a perfect score.')
  


