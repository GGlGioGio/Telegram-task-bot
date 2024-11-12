# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт Flask-приложения
EXPOSE 5000

# Запуск приложения
CMD ["python", "bot.py"]
