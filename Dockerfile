FROM python:3.7-alpine3.10

COPY . /deploy/app/privatepypi
WORKDIR /deploy/app/privatepypi

RUN pip install -r requirements.txt

CMD ./privatepypi.sh