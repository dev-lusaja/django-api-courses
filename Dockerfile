FROM python:3.11-alpine

WORKDIR /code

COPY requirements.txt /requirements.txt

ADD api /code

RUN pip install -r /requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]