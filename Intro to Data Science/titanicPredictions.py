import numpy as np
import pandas as pd

df = pd.read_csv("titanic_data.csv")

predictions = {}

def calculateAccuracy(predictions, df):
    count = 0
    for id, survived in predictions.items():
        true_survival = df['Survived'][df['PassengerId'] == id].values
        if survived == true_survival:
            count += 1
    
    total = df['PassengerId'].count()
    answer = str(round(count/total, 3) * 100)
    return answer + '%'

#Hueristic Using only Age
female_id = df['PassengerId'][df['Sex'] == "female"]
male_id =  df['PassengerId'][df['Sex'] == "male"]

for id in female_id:
    predictions[id] = 1

for id in male_id:
    predictions[id] = 0

accuracy = calculateAccuracy(predictions, df)
print('Accuracy with Sex Hueristic: ')
print(accuracy)
print()


#Hueristic Using Sex, Age, and Class
survived = []
died = []
for index, row in df.iterrows():
    if row['Sex'] == "male":
        if row['Pclass'] == 1 and row['Age'] < 18:
            survived.append(row['PassengerId'])
        else:
            died.append(row['PassengerId'])
    else:
        survived.append(row['PassengerId'])

for id in survived:
    predictions[id] = 1

for id in died:
    predictions[id] = 0

accuracy = calculateAccuracy(predictions, df)
print('Accuracy with Sex, Age, and Class Hueristic: ')
print(accuracy)
print()

#Hueristic Using Random
survived = []
died = []
for index, row in df.iterrows():
    if row['Sex'] == "male":
        if row['Pclass'] == 1 and row['Age'] < 19:
            survived.append(row['PassengerId'])
        else:
            if row['Fare'] > 100:
                survived.append(row['PassengerId'])
            else:
                died.append(row['PassengerId'])
    else:
        survived.append(row['PassengerId'])

for id in survived:
    predictions[id] = 1

for id in died:
    predictions[id] = 0

accuracy = calculateAccuracy(predictions, df)
print('Accuracy with Sex=F, Age<19, Class=1, and Fare>100 Hueristic: ')
print(accuracy)
print()

survived = []
died = []
for index, row in df.iterrows():
    if row['Sex'] == "male":
        if row['Pclass'] == 1 and row['Age'] < 18:
            survived.append(row['PassengerId'])
        else:
            if row['Fare'] > 150:
                survived.append(row['PassengerId'])
            else:
                died.append(row['PassengerId'])
    else:
        if row['Pclass'] < 3:
            survived.append(row['PassengerId'])
        else:
            if row['Age'] < 30:
                survived.append(row['PassengerId'])
            else:
                died.append(row['PassengerId'])

for id in survived:
    predictions[id] = 1

for id in died:
    predictions[id] = 0

accuracy = calculateAccuracy(predictions, df)
print('Accuracy with Custom Hueristic: ')
print(accuracy)
print()

survived = []
died = []
for index, row in df.iterrows():
    if row['Sex'] == "male":
        if row['Pclass'] ==1 and row['Age'] < 18:
            survived.append(row['PassengerId'])
        else:
            if row['Fare'] > 200:
                survived.append(row['PassengerId'])
            else:
                died.append(row['PassengerId'])
    else:
        if row['Pclass'] < 3:
            survived.append(row['PassengerId'])
        else:
            if row['Age'] < 30 and row['SibSp'] < 2:
                survived.append(row['PassengerId'])
            else:
                died.append(row['PassengerId'])

for id in survived:
    predictions[id] = 1

for id in died:
    predictions[id] = 0

accuracy = calculateAccuracy(predictions, df)
print('Accuracy with Custom Hueristic: ')
print(accuracy)
print()

survived = []
died = []
for index, row in df.iterrows():
    if row['Sex'] == "male":
        if row['Pclass'] ==1 and row['Age'] < 18:
            survived.append(row['PassengerId'])
        else:
            if row['Pclass'] ==2 and row['Age'] < 16:
                survived.append(row['PassengerId'])
            else:
                if row['Fare'] > 200:
                    survived.append(row['PassengerId'])
                else:
                    died.append(row['PassengerId'])
    else:
        if row['Pclass'] < 3:
            survived.append(row['PassengerId'])
        else:
            if row['Age'] < 30 and row['SibSp'] < 2:
                survived.append(row['PassengerId'])
            else:
                died.append(row['PassengerId'])

for id in survived:
    predictions[id] = 1

for id in died:
    predictions[id] = 0

accuracy = calculateAccuracy(predictions, df)
print('Accuracy with Custom Hueristic: ')
print(accuracy)
print()