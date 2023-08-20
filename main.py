import requests

API_key='c36156d1ccf4700f15af4ef3'
url='https://v6.exchangerate-api.com/v6/'+API_key+('/latest'
                                                 '/USD')
response = requests.get(url)
data = response.json()
print('Data acquired from API')

top=['USD','EUR','JPY','GBP','AUD','CAD','CHF','CNY','HKD','NZD']
for i in top:
    print(i,':',data['conversion_rates'][i])

import psycopg2
import pandas as pd

conn = psycopg2.connect("dbname=web user=postgres password=admin")
cur = conn.cursor()
sql='CREATE TABLE IF NOT EXISTS currency (id serial PRIMARY KEY, currency VARCHAR(3), rate FLOAT)'
cur.execute(sql)
conn.commit()
print('Table created')

for i in top:
    #Update the table if the currency already exists
    sql='UPDATE currency SET rate=%s WHERE currency=%s'
    cur.execute(sql,(data['conversion_rates'][i],i))
    conn.commit()
    #If the currency does not exist, insert it
    sql='INSERT INTO currency (currency, rate) SELECT %s,%s WHERE NOT EXISTS (SELECT 1 FROM currency WHERE currency=%s)'
    cur.execute(sql,(i,data['conversion_rates'][i],i))
    conn.commit()
print('Data inserted')

