import psycopg2
from tkinterApp import tkinterApp
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

# Driver Code
win = tkinterApp()
cursor.close()
connection.close()
