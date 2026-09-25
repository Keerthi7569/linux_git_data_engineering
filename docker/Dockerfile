FROM python:3.14-slim

WORKDIR /app

COPY scripts/api_extract.py .

RUN pip install --no-cache-dir requests

CMD ["python", "api_extract.py"]
