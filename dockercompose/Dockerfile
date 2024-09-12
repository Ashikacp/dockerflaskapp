FROM python:3.9-alpine   
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# from local repository we are copying content to working dir
COPY . . 
RUN pip install -r requirements.txt 
EXPOSE 5001
CMD ["flask","run","--host=0.0.0.0", "--port=5001"]
#i have given host and port since my 5000 port is already in use.

