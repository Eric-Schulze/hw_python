import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats

#Predict number of homeruns from height and weight data using regression with gradient descent

#need baseball_stats.csv
#features = height, weight
#values = HR (homeruns, observedY)
#define theta as an array of random values 0.0-1.0 with normal distribution

def compute_cost(features, values, theta):
    m = len(values) #number of data points
    sum_of_square_errors = np.square(np.dot(features,theta) - values).sum()
    cost = sum_of_square_errors / (2 * m)
    return cost
    
    
#use small value for alpha, around 0.1
def gradient_descent(features, values, theta, alpha, num_iterations):
    m = len(values) #number of data points
    print(m)
    cost_history = []
    for i in range(num_iterations):
        predicted_values = np.dot(features,theta)
        print(predicted_values)
        test = np.dot(features.T,(predicted_values - values))
        print(test)
        theta = theta - ( alpha / m ) * np.dot(features.T,(predicted_values - values))
        cost = compute_cost(features, values, theta)
        cost_history.append(cost)
    return theta, pd.Series(cost_history)
    

theta = [[0.7], [0.3]]

df = pd.read_csv('baseball_stats.csv')

features = df[['height','weight']]

features = features.applymap(lambda x: x.replace(' ',''))

features['height'] = pd.to_numeric(features['height'])
features['weight'] = pd.to_numeric(features['weight'])

features = features.fillna(features.mean()[['height','weight']])

values = df[['HR']]
values = values.fillna(values.mean()[['HR']])

features = (features - features.mean())/features.std()
values = (values - values.mean())/values.std()

alpha = 0.1
num_iterations = 1000
prediction = gradient_descent(features,values,theta,alpha,num_iterations)

print(prediction)
