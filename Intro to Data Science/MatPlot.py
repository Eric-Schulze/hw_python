import pandas as p
import numpy as n
import matplotlib.pyplot as m

#initial set of baby names and births
names = ['Bob','Jessica','Mary','John','Mel']
births = [968,155,77,578,973]

#zip: merge two lists
BabyDataSet = list(zip(names,births))
print(BabyDataSet)
print()

#create a dataframe from the list
df = p.DataFrame(data=BabyDataSet, columns=['Names','Births'])
print(df)
print()

#export dataframe to a csv file; generated in current working directory
df.to_csv('births1880.csv', index=False, header=True)

#prefix string with char 'r' to escape the whole string
Location = r'births1880.csv'

ndf = p.DataFrame(p.read_csv(Location))
print(ndf)
print()
print(ndf.dtypes) #print data type
print(ndf.describe()) #gives basic stats of data
print()

#Find the most popular name (multiple approaches)
#Sort and pick top value

sorted = df.sort_values(['Births'], ascending=False)
print(sorted.head(1))
print()

#Or, return max
print(df['Births'].max())
maxName = df['Names'][df['Births'] == df['Births'].max()].values
print(maxName)
print()

#Plotting
'''
df['Births'].plot()
m.show()
'''

emp = p.DataFrame(p.read_csv(r'employee.csv'))

emp['Annual_Salary'] = p.to_numeric((emp['Annual_Salary'].apply(lambda x: x[1:])).apply(lambda x: x.replace(',','')))

sorted_emp = emp.sort_values(['Annual_Salary'],ascending=False)
print(sorted_emp.head(1))
'''
max_string = str(emp['Annual_Salary'][emp['Annual_Salary_Float'] == emp['Annual_Salary_Float'].max()].values)
print("Max Salary: " + max_string)
'''



