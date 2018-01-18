import pandas as pd

baseball_data = pd.read_csv('Master.csv')

#add values in tow columns and write to a new csv file
baseball_data['height_plus_weight'] = baseball_data['height'] + baseball_data['weight']

baseball_data[['nameLast','nameGiven','height_plus_weight']].to_csv('heightplusweight.csv',                                                                                                           index=False, 
                                                                                                           header=False)

baseball_data['fullname'] = baseball_data['nameGiven'] + ' ' + baseball_data['nameLast']

baseball_data[['fullname','birthCountry']].to_csv('playerlocation.csv', index=False, header=False)

#Find how many players are from Venezuela

num_from_venezuela = baseball_data['birthCountry'].value_counts()['Venezuela']
print(num_from_venezuela)

