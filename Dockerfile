#Python base image(usually a linux image) based on Alpine Linux
FROM python:3.9-alpine   

#  . This refers to the current directory on your host machine , /app: This is the destination directory inside the Docker container.
COPY . /app                   

WORKDIR /app

RUN pip install -r requirements.txt

CMD python app.py 

