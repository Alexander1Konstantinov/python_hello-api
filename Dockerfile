FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения
COPY . .

# Указываем стандартный порт Uvicorn (8000)
EXPOSE 8000

# Запускаем приложение (используем параметры по умолчанию)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]