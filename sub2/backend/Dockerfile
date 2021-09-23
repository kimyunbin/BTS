
FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install django djangorestframework mysqlclient djangorestframework-jwt
RUN pip install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 mange.py migrate
COPY . .

EXPOSE 8000

CMD ["gunicorn","--bind","0.0.0.0:8000", "backend.wsgi:application"]

