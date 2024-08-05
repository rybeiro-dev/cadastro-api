FROM python:3.9

RUN apt-get update && apt-get install -y default-mysql-client

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY wait-for-db.sh /usr/local/bin/wait-for-db.sh

RUN chmod +x /usr/local/bin/wait-for-db.sh

ENTRYPOINT ["/usr/local/bin/wait-for-db.sh", "python", "main.py"]
