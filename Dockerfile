FROM python:3.11-slim
RUN apt-get update; apt-get install -y gcc libpq-dev; pip install --upgrade pip; apt-get upgrade;
WORKDIR /code
COPY . /code
RUN pip install --no-cache-dir -r /code/requirements.txt
ENV MODE dev

EXPOSE 8090

CMD ["uvicorn", "app.main:app","--host", "0.0.0.0" ,"--port", "8090"]