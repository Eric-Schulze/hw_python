import pandas as pd
import pandasql as pds
import sqlite3 as sl3
from datetime import datetime

#create a connection object
con = sl3.connect('flights.db')

#create cursor for executing queries
cur = con.cursor()

#execute a query
cur.execute("select * from airlines limit 5")

#extract data from cursor object
result = cur.fetchall()

print(result)

airline_df = pd.DataFrame(data=result)

print(airline_df)
print()

cur.execute("select name,city from airports group by country")
airports = cur.fetchall()

print(airports)
print()

df1 = pd.read_sql_query("select * from routes limit 5", con)
print(df1)
print()


df_flights = pd.read_sql_query("select * from airlines limit 5", con)
print(df_flights)
print()

#add tuple to a table in the db
cur.execute("insert into airlines values (6048,19846,'Test flight','','',null,null,null,'Y')")
#cur.execute(insert.....) generates a flight.db-journal
con.commit()
print(pd.read_sql_query("select * from airlines where id=19846",con))

values = ('USA',19846)
cur.execute("update airlines set country=? where id=?", values)
con.commit()
print(pd.read_sql_query("select * from airlines where id=19846",con))
print()

#delete a tuple
values = (19846,)
cur.execute("delete from airlines where id=?",values)
con.commit()
print(pd.read_sql_query("select * from airlines where id=19846",con))
print()

#create a new table
cur.execute("drop table my_daily_flights")
con.commit()
cur.execute("create table my_daily_flights(id int, departure date, arrival date, number text, route_id integer)")
con.commit()

cur.execute("insert into my_daily_flights values(1,'2017-05-18 3:35','2017-05-19 9:55','T1',1)")
con.commit()
print(pd.read_sql_query("select * from my_daily_flights"),con)
print()

#create table with pandas df
flightdf = pd.DataFrame([[1, datetime(2017,05,17,3,35), datetime(2017,05,19,9,55), 'T1',1]], columns=["id","departure","arrival","number","route_id"])


#convert df to a table, replace if exists
flightdf.to_sql("another_daily_flights", con, if_exists="replace")
print(pd.read_sql_query("select * from another_daily_flights",con))
print()

#alter the table, no commit necessary
cur.execute("alter table another_daily_flights add column airplanes integer")
print(pd.read_sql_query("select * from another_daily_flights",con))
print()



cur.close()
con.close() #unlocks db
