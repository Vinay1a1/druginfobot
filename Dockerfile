FROM python:3.12-slim

WORKDIR /app

RUN groupadd -g 1000 botgroup && \
    useradd -m -u 1000 -g botgroup botuser

RUN python3 -m venv tgbot

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R botuser:botgroup /app
USER 1000

CMD ["python", "main.py"]