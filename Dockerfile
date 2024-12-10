FROM python:3.12.8-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt
COPY scripts/ /app/scripts/
COPY datalake/ /app/datalake

RUN apt-get update && apt-get install -y \
    default-jdk \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt


EXPOSE 8000

CMD ["sh", "-c","python scripts/pipeline_etl.py; tail -f /dev/null"]

