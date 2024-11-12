import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from db import create_connection, create_table

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Команды бота
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your task bot!')

def add_task(update: Update, context: CallbackContext) -> None:
    task_name = ' '.join(context.args)
    
    if task_name:
        connection = create_connection()  # Создаем подключение
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tasks (task_name) VALUES (%s)", (task_name,))
        connection.commit()
        cursor.close()
        connection.close()
        update.message.reply_text(f"Task '{task_name}' added.")
    else:
        update.message.reply_text("Please provide a task name.")

def list_tasks(update: Update, context: CallbackContext) -> None:
    connection = create_connection()  # Создаем подключение
    cursor = connection.cursor()
    cursor.execute("SELECT id, task_name, status, priority FROM tasks")
    tasks = cursor.fetchall()
    
    message = "Your tasks:\n"
    for task in tasks:
        message += f"ID: {task[0]} | Task: {task[1]} | Status: {task[2]} | Priority: {task[3]}\n"
    
    update.message.reply_text(message)
    cursor.close()
    connection.close()

def main() -> None:
    # Создание базы данных и таблицы
    create_table()  # Создаём таблицу при запуске бота

    # Получение токена и запуск бота
    token = os.getenv('7326991752:AAFwoc4FVxMwQDPwdvzMkun_MyKVO44Bxcc')  # Теперь берем токен из переменных окружения
    updater = Updater(token)

    dispatcher = updater.dispatcher

    # Добавляем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("add", add_task))
    
