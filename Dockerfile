# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем локальные файлы в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем, что контейнер будет слушать на порту 5000
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]
