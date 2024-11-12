import psycopg2
import os

def create_connection():
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host="db",  # Имя контейнера с базой данных
            port="5432"
        )
        return connection
    except Exception as error:
        print(f"Ошибка при подключении к базе данных: {error}")
        return None

def create_table():
    # Создаем подключение к базе данных
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        
        # SQL-запрос для создания таблицы
        create_table_query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            task_name TEXT NOT NULL,
            status TEXT DEFAULT 'in progress',
            priority TEXT DEFAULT 'low'
        );
        """
        
        # Выполнение запроса
        cursor.execute(create_table_query)
        connection.commit()
        
        # Закрытие курсора и соединения
        cursor.close()
        connection.close()
        print("Table created successfully!")
    else:
        print("Failed to connect to the database, table was not created.")
