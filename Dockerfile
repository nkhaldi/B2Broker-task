FROM python:3.11

WORKDIR /src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
