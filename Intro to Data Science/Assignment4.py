import numpy as np
import scipy as sp
from scipy import stats
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

df = pd.read_csv('turnstile_data_master_with_weather.csv')

#Part 1
#Instructions were unclear about how to specifically build the turnstile_weather dataframe
#I was unable to get a histogram to plot the correct axes and could not find any documentation supporting how to switch axes, not just move horizontal, so I use a bar graph

entries_rain = df[['ENTRIESn_hourly', 'Hour']][df['rain'] == 1]
entries_no_rain = df[['ENTRIESn_hourly', 'Hour']][df['rain'] == 0]

entries_rain = entries_rain.rename(columns = {'ENTRIESn_hourly':'rain_hourly_entries'})
entries_no_rain = entries_no_rain.rename(columns = {'ENTRIESn_hourly':'no_rain_hourly_entries'})

entries_rain = entries_rain.groupby(['Hour'])
entries_no_rain = entries_no_rain.groupby(['Hour'])

entries_rain_total = entries_rain.sum()
entries_no_rain_total = entries_no_rain.sum()

entries = pd.concat([entries_rain_total, entries_no_rain_total], axis=1)

entries.plot.bar(alpha=0.5)

plt.show()


#Part 2

print('Mean Entries Per Hour (Rain): ')
print(round(entries_rain.mean(),1))
print()
print('\nMean Entries Per Hour (No Rain): ')
print(round(entries_no_rain.mean(),1))
print()

print('Mann Whitney U-Test:')
print(sp.stats.mannwhitneyu(entries_rain_total, entries_no_rain_total, alternative='less'))

print()
print('There is not statistical difference between rain and no rain days')
print()

#Part 3
#Since weather related data does not change between data for a single day, I made the assumption that the regression should be to predict the number of riders on a given day, not a given hour. Best R^2 value: 0.25555

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
    
def r_squared(predictions, values):
    sst = ((values - np.mean(values))**2).sum()
    ssr = ((predictions - values)**2).sum()
    r_sq = 1 - ssr / sst
    return r_sq
    

features = df[['precipi','rain', 'mintempi', 'meantempi', 'maxtempi', 'minpressurei', 'meanpressurei', 'mindewpti', 'meandewpti', 'meanwindspdi', 'maxpressurei', 'maxdewpti', 'DATEn']]
features = features.interpolate()
features = features.groupby('DATEn')
features = features.mean()

theta = [[0.1],[0.1], [0.05], [0.2], [0.05], [0.05], [0.05], [0.05], [0.05], [0.1],[0.1], [0.1]]

values = df[['ENTRIESn_hourly', 'DATEn']]
values = values.interpolate()
values = values. groupby('DATEn')
values = values.sum()


features = (features - features.mean())/features.std()
values = (values - values.mean())/values.std()

alpha = 0.1
num_iterations = 10000
prediction_theta, cost_history = gradient_descent(features,values,theta,alpha,num_iterations)

predictions = np.dot(features, prediction_theta)
r_sq = r_squared(predictions, values)

print('Original Theta: ' + str(theta))
print('Prediction Theta: ' + str(prediction_theta))
print('Alpha: ' + str(alpha))
print('Number of Iterations:' + str(num_iterations))
print('Cost History: ')
print(cost_history)
print()
print('R-Squared: ' + str(r_sq))


