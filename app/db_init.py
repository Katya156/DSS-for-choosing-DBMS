import psycopg2
import os

def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )

def initialize_database():
    connection = get_conn()
    cursor = connection.cursor()

    # Пример создания таблицы
    cursor.execute("""
        CREATE SEQUENCE code_seq START WITH 1 INCREMENT BY 1;
        CREATE TABLE IF NOT EXISTS criteria (
            id NUMERIC(5) DEFAULT NEXTVAL('code_seq') PRIMARY KEY,
            criteria_name VARCHAR(100) NOT NULL,
            criteria_types_name VARCHAR(40) REFERENCES criteria_types(criteria_type_name) NOT NULL,
            data_types_name VARCHAR(20) REFERENCES data_types(data_type_name) NOT NULL,
            adding_date DATE NOT NULL,
            termination_date DATE,
            minimum_value VARCHAR(40),
            maximum_value VARCHAR(40),
            unit VARCHAR(10),
            comment VARCHAR(120)
        );
        ALTER SEQUENCE code_seq OWNED BY criteria.id;
    """)

    # Пример вставки начальных данных
    cursor.execute("""
        insert into criteria values
        (2, 'К1.1. Используемая модель данных', 'диапазон', 'varchar', current_date, null, null, null),
        (3, 'К1.2. Триггеры и хранимые процедуры', 'бинарный', 'varchar', current_date, null, null, null),
        (4, 'К1.3. Предусмотренные типы данных', 'список', 'varchar', current_date, null, null, null),
        (6, 'К2.1. Масштабируемость', 'список', 'varchar', current_date, null, null, null),
        (7, 'К2.2. Распределенность', 'бинарный', 'varchar', current_date, null, null, null),
        (9, 'К3.1. Контроль использования памяти компьютера', 'бинарный', 'varchar', current_date, null, null, null),
        (10, 'К3.2. Автонастройка', 'бинарный', 'varchar', current_date, null, null, null),
        (12, 'К4.1. Наличие средств разработки приложений', 'бинарный', 'varchar', current_date, null, null, null),
        (13, 'К4.2. Наличие средств проектирования', 'список', 'varchar', current_date, null, null, null),
        (14, 'К4.3. Наличие многоязыковой поддержки', 'список', 'varchar', current_date, null, null, null),
        (15, 'К4.4. Поддерживаемые языки программирования', 'список', 'varchar', current_date, null, null, null),
        (17, 'К5.1. Минимальный рейтинг транзакций', 'диапазон', 'numeric', current_date, null, 1, 1000000, null, TPS),
        (19, 'К6.1. Восстановление после сбоев', 'список', 'varchar', current_date, null, null, null),
        (20, 'К6.2. Резервное копирование', 'список', 'varchar', current_date, null, null, null),
        (21, 'К6.3. Откат изменений', 'список', 'varchar', current_date, null, null, null),
        (22, 'К6.4. Многоуровневая система защиты', 'список', 'varchar', current_date, null, null, null),
        (23, 'К7. Требования к рабочей среде', ),
        (24, 'К7.1. Поддерживаемые аппаратные платформы', 'список', 'varchar', current_date, null, null, null),
        (25, 'К7.2. Минимальная тактовая частота процессора', 'диапазон', 'numeric', current_date, null, 1.0, 4.0, null, GHz),
        (26, 'К7.3. Максимальный размер адресуемой памяти', 'диапазон', 'numeric', current_date, null, 0, 4000, null, GB),
        (27, 'К7.4. Поддерживаемые операционные системы', 'список', 'varchar', current_date, null, null, null),
        (29, 'К8.1. Максимальная стоимость лицензии', 'диапазон', 'numeric', current_date, null, 0, 25000, null, USD),
        (30, 'К8.2. Рейтинг СУБД', 'диапазон', 'numeric', current_date, null, 1, 100, null, null)
        ON CONFLICT DO NOTHING;
    """)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    initialize_database()
