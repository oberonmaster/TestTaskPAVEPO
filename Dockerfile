# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт приложения
EXPOSE 8000

# Запуск сервера FastAPI
CMD ["uvicorn", "audio_service.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
