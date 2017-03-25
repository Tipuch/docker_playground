FROM python:3.5
ADD . /docker_playground
WORKDIR /docker_playground
RUN pip install -Ur requirements.txt
RUN python manage.py migrate
