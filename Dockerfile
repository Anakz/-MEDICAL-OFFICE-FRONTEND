FROM ubuntu
# FROM python:3.10.4-slim-buster

# WORKDIR /app

# COPY requirements.txt requirements.txt

# RUN pip3 install -r requirements.txt

# COPY . .

# CMD [ "python", "project/manage.py", "runserver", "0.0.0.0:8765" ]

# -------------------------------------------
# FROM python:3.10.4-slim-buster

# ENV PYTHONUNBUFFERED 1

# RUN mkdir /app

# WORKDIR /app

# COPY ./requirements.txt /app/

# COPY ./project/ /app/

# RUN pip install -r requirements.txt

# -------------------------------------------

# COPY ./requirements.txt /app/requirements.txt

# WORKDIR /app

# RUN python -m venv env

# RUN env/Scripts/activate

# RUN pip install -r requirement.txt

# COPY ./project /app

# CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8085

# CMD ["python", "manage.py", "runserver"]