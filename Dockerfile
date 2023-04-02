FROM python:3.11-alpine

WORKDIR /code

COPY requirements.txt /requirements.txt

COPY api /code

RUN pip install -r /requirements.txt

EXPOSE 8000

CMD ["manage.py", "runserver", "0.0.0.0:8000"]

ENTRYPOINT ["python3"]