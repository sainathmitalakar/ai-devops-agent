FROM python:3.11-slim

WORKDIR /app

COPY agent/ ./agent
COPY .env .env

RUN pip install --no-cache-dir -r agent/requirements.txt

CMD ["python", "agent/main.py"]