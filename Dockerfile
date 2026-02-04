FROM python:3.15.0a5-slim

WORKDIR /app

RUN python3 -m venv tgbot

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN sed -i 's/\r$//' *.sh

CMD ["python", "main.py"]