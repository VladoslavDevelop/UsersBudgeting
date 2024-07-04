FROM python:3.8-alpine

RUN apk update && apk add --no-cache bash gcc musl-dev linux-headers \
    jpeg-dev zlib-dev mariadb-dev libffi-dev

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]