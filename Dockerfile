FROM python:3.12-slim

WORKDIR /app

RUN python3 -m venv tgbot

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]