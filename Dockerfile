FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR .

RUN apt update && pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
