import numpy as n

numbers = [1,2,3,4,5,6]
print("MEAN: " + str(n.mean(numbers)))
print("Median: " + str(n.median(numbers)))
print("STD: " + str(n.std(numbers)))
num = n.array([1,2,3,4,5,6])
num = num/3.0
print(num)

num[2:5] = 15.75
print( num[0:5])

two_D = n.array([[1,2,3],[4,5,6]],float)
print(two_D)
print("")

#2D array slicing
print(two_D[1][1])
print()
print(two_D[1,:])
print()
print(two_D[:, 2])
print()


#Some arithmetic operations on arrays
array1 = n.array([1,2,3],float)
array2 = n.array([5,6,7],float)

print(array1 + array2)
print()
print(array1 - array2)
print()
print(array1*array2)
print()

array2d1 = n.array([[1,2],[3,4]], float)
array2d2 = n.array([[5,6],[7,8]], float)
print(array2d1 + array2d2)
print()
print(array2d1 - array2d2)
print()
print(array2d1*array2d2)
print()

import pandas as p

'''
Series is similar to one-dimensional object that is similar to an array, list, or a column in a database;
0 based indexing
'''
series1 = p.Series(['Alan','Grant','TN',45,-17])
print(series1)
print()

series2 = p.Series(['Dave','Lewis','KY',39,-9], index = ['first_name','last_name','state','age','demerits'])
print(series2)
print()

series3 = p.Series([1,2,3,39,9], index = ['first_name','last_name','state','age','demerits'])
print(series3)

#Use indexing to select specific items
print()
print(series2['state'])
print()
print(series2[['first_name','last_name','age']])
print()

cuteness = p.Series([1,2,3,4,5], index=['bug','fish','pig','puppy','kitten'])
print(cuteness)
print()
print(cuteness > 3)
print()
print(cuteness[cuteness > 3])
print()

'''
Think of a DataFrame as something with rows and columns.
Similar to a spreadsheet or R's data.frame
'''

data = {'year':[2010,2011,2012,2011,2012],
             'team':['Bears','Bears','Bears','Packers','Packers'],
             'wins':[11,8,10,15,11],
             'losses':[5,8,6,1,5]}

football = p.DataFrame(data)
print(football)

d = {'one': p.Series([1,2,3], index=['a','b','c']),
        'two': p.Series([1,2,3,4], index=['a','b','c','d'])}
df = p.DataFrame(d)
print()
print(df)
print()

#functions: apply, map, applymap

#"apply" performs the function (taken as an argument) on the vector that is every single column, and returns a dataframe
print(df.apply(n.mean)) 
print()

#walkthrough each value in given column and evaluate the given function on each value
#map only works on a single vector
print(df['one'].map(lambda x: x >= 1))
print()

#applymap will map a function across an entire dataframe (or map it on each vector within a dataframe)
print(df.applymap(lambda x: x >=1))
print()

#numpy.dot  Matrix dot product
a = [1,2,3,4,5]
b = [2,3,4,5,6]
print(n.dot(a,b))
print()

c = [1,2]
d = [[2,4,6],[3,5,7]]

print(n.dot(c,d))
print()
