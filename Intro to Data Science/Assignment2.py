#Programming Assignment 2
import pandas as pd
import numpy as np
import sqlite3 as sl3
from datetime import datetime
import pandasql as pds
import json
import requests

df_aadhaar = pd.read_csv('aadhaar_data.csv')

df_aadhaar.rename(columns=lambda x: x.replace(' ','_').lower(), inplace=True)

# Q1. Find out the total number of cards approved by states.
df_approved = df_aadhaar['pin_code'][df_aadhaar['aadhaar_generated'] > 0]
print('Q1) Total number of cards approved: ')
print(df_approved.count())
print()

# Q2. Find out the total number of cards rejected by states.
df_rejected = df_aadhaar['pin_code'][df_aadhaar['enrolment_rejected'] > 0]
print('Q2) Total number of cards rejected: ')
print(df_rejected.count())
print()

# Q3. Find out the total number of Aadhaar applicants by gender.
print('Q3) Total number of applicants by gender:')
print(df_aadhaar['gender'].value_counts())
print()

# Q4. Find out the total number of Aadhaar applicants by age groups less than 25, between 25 -- 55, and over 55.
df_young = df_aadhaar['pin_code'][df_aadhaar['age'] < 25]
df_mid = df_aadhaar['pin_code'][(df_aadhaar['age'] >= 25) & (df_aadhaar['age'] <= 55)]
df_old = df_aadhaar['pin_code'][df_aadhaar['age'] > 55]
print('Q4) Total number of applicants by age group: ')
print('Age less than 25: ' + str(df_young.count()))
print('Age between 25 and 55: ' + str(df_mid.count()))
print('Age older than 55: ' + str(df_old.count()))
print()

#Q5.  Run a SQL query on a data-frame of weather data. The SQL query should return one column and one row - a count 
#of the number of days in the data-frame where the rain column is equal to 1 (i.e., the number of days it rained). 
df_weather = pd.read_csv('weather_underground.csv')

query = 'select count("date") as rainy_days from df_weather where rain = 1'

print('Q5) Total days of rain:')
print(pds.sqldf(query.lower(), locals()))
print()

#Q6. Run a SQL query on a data-frame of weather data that it returns two columns and two rows - 
#whether it was foggy or not (0 or 1) and the max maxtempi for that fog value (i.e., the maximum max 
#temperature for both foggy and non-foggy days). 
query = 'select fog, MAX(maxtempi) as max_temp from df_weather group by fog'
print('Q6) Max temp with fog:')
print(pds.sqldf(query.lower(), locals()))
print()

# Q7. Run a SQL query on a data-frame of weather data that it returns one column and
#one row - the average meantempi on days that are a Saturday or Sunday (i.e., the the 
#average mean temperature on weekends).
query = 'select avg(meantempi) as mean_temp from df_weather where cast(strftime("%w", date) as integer) IN (5,6)'
print('Q7) Mean temp on Saturdays and Sundays:')
print(pds.sqldf(query.lower(), locals()))
print()

#Q8. Create a database (music) table by extracting top-artists data as a JSON file from 
#https://www.last.fm/api/ (Links to an external site.)Links to an external site. for India. 
#Name your table TopIndianListners. The table should have two columns; 
#name of the artist and number of listeners. 
geo_url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&api_key=4005c05d541d9a056136d5450be12883&country=india&format=json'

df_music = pd.read_json(geo_url,orient='index')

#print('Readable : ', json.dumps(geo_data,indent=4))
print(df_music)


# Q8.1 Run a SQL query on your table to find the artist with highest number of listeners.

# Q8.2 Run a SQL query on your table to find all artists with more than a million listeners.
      
      
      
      
      
      