import pandas as pd
import pandasql as pds


aadhaar_data = pd.read_csv('aadhaar_data.csv')

aadhaar_data.rename(columns=lambda x: x.replace(' ','_').lower(), inplace=True)

#using SQLite syntax
q = "SELECT * FROM aadhaar_data LIMIT 20"

sqlsolution = pds.sqldf(q.lower(), locals())
print()
print(sqlsolution)
print()

q2 = "Select district,sub_district,sum(aadhaar_generated) from aadhaar_data where age > 50 group by district, sub_district"

sqlsolution2 = pds.sqldf(q2.lower(), locals())

print(sqlsolution2)
print()




