FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /RESTFULAPICRUD
COPY requirements.txt /RESTFULAPICRUD/
RUN pip install -r requirements.txt
COPY . /RESTFULAPICRUD/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
