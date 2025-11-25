FROM python:3.10-slim

WORKDIR /app

RUN pip install requests

COPY client.py .

CMD ["python", "client.py"]
