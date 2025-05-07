import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os
from collections import defaultdict

# Загружаем данные из .env файла
load_dotenv()

# Подключаемся к базе
connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=""
)
cursor = connection.cursor()

dbms_values = []
cursor.execute('''select distinct criteria_name, version_name, value_
                            from dbms_values a
                                join criteria b
                                    on a.criteria_id = b.id
                                join dbms_versions c
                                    on a.dbms_version_id = c.id''')
rows = cursor.fetchall()
for i in rows:
    criteria_name = i[0]
    version_name = i[1]
    value = int(i[2])
    dct = {}
    if criteria_name.split()[0].count('.') > 1:
        dct['criteria'] = criteria_name
        dct['alternatives'] = version_name
        dct['values'] = value
    dbms_values.append(dct)

dbms_values = pd.DataFrame(dbms_values)
dbms_values = dbms_values.pivot(index="alternatives", columns="criteria", values="values")


dbms_values.to_excel('res.xlsx')