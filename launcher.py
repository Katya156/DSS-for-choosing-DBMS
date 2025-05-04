import psycopg2
import subprocess
import os
import time
import sys
from dotenv import load_dotenv

load_dotenv()

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

PG_DATA = resource_path("pg/data")

def start_postgres():
    if not os.path.exists(PG_DATA):
        subprocess.run([resource_path("pg/bin/initdb.exe"), "-D", PG_DATA, "--encoding=UTF8"])
        print("Инициализация базы данных...")

    logfile_path = resource_path("pg/data/logfile.txt")

    result = subprocess.run([
        resource_path("pg/bin/pg_ctl.exe"),
        "-D", PG_DATA,
        "-o", f"-p {os.getenv('DB_PORT')}",
        "-l", logfile_path,
        "start"
    ])

    if result.returncode == 0:
        print("PostgreSQL запущен.")
    else:
        print("PostgreSQL не запущен.")
    time.sleep(3)

def restore_data():
    try:
        # Подключаемся к базе
        try:
            connection = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                dbname=os.getenv("DB_NAME"),
                # 'postgres',
                # os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS")
            )
            print('Подключение прошло успешно')
        except psycopg2.OperationalError as e:
            print('Не удалось подключиться к базе данных:', e)

        connection.autocommit = True
        cur = connection.cursor()

        # # Проверяем, есть ли база с именем apitone
        cur.execute("SELECT 1 FROM pg_database WHERE datname = 'apitone';")
        exists = cur.fetchone()

        # cur.execute("""
        #             SELECT pg_terminate_backend(pid)
        #             FROM pg_stat_activity
        #             WHERE datname = 'apitone' AND pid <> pg_backend_pid();
        #         """)
        #
        # # Удаляем базу, если она существует
        # cur.execute("DROP DATABASE IF EXISTS apitone;")

        if not exists:
            print("Создаём базу apitone и восстанавливаем данные...")

            cur.execute("CREATE DATABASE apitone ENCODING 'UTF8' TEMPLATE template0;")
            connection.close()

            # Восстанавливаем дамп
            subprocess.run([
                resource_path("pg/bin/psql.exe"),
                "-U", "postgres",
                "-d", "apitone",
                "-p", os.getenv("DB_PORT"),
                "-f", resource_path("data/init_db.sql")
            ],  env={**os.environ, "PGCLIENTENCODING": "UTF8"})
        else:
            print("База apitone уже существует. Восстановление не требуется.")

    except Exception as e:
        print("Ошибка при восстановлении базы данных:", e)

def stop_postgres():
    subprocess.run([
        resource_path("pg/bin/pg_ctl.exe"),
        "-D", PG_DATA,
        "stop",
        "-m", "fast"  # "smart", "fast" или "immediate"
    ])
    print("PostgreSQL остановлен.")

def run_app():
    subprocess.run(["python", resource_path("main.py")])

if __name__ == "__main__":
    try:
        start_postgres()
        restore_data()
        run_app()
    finally:
        stop_postgres()