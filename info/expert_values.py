import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

# Загружаем данные из .env файла
load_dotenv()

# Подключаемся к базе
connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS")
)

cursor = connection.cursor()

alternatives = ['Oracle Database 19c', 'PostgreSQL 13', 'MySQL 9.1 IR', 'SQL Server 2022']

criteria = []
cursor.execute('''select distinct id, criteria_name from criteria order by id''')
rows = cursor.fetchall()
for i in rows:
    name = i[1]
    if name.split()[0].count('.') > 1:
        criteria.append(name)

data = [
    # Oracle Database 19c
    [10, 10, 10, 9, 9, 9, 10, 10, 9, 10, 10, 9, 10, 10, 10, 10, 10, 8, 10, 10, 2, 10],
    # PostgreSQL 13
    [9, 9, 9, 8, 8, 8, 8, 7, 7, 9, 9, 7, 8, 8, 8, 9, 8, 7, 8, 9, 10, 8],
    # MySQL 9.1 IR
    [8, 8, 8, 7, 6, 7, 7, 6, 6, 7, 8, 6, 7, 7, 7, 8, 7, 6, 7, 8, 10, 7],
    # SQL Server 2022
    [9, 10, 9, 9, 8, 9, 9, 10, 9, 9, 9, 9, 9, 9, 9, 10, 9, 8, 9, 9, 5, 9],
]

expert_values = pd.DataFrame(data, columns=criteria, index=alternatives)

