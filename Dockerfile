FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY ./requirements/ /code/requirements/
RUN pip install --upgrade pip
RUN pip install -r ./requirements/base.txt

ADD . /code/