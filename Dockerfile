FROM python:3.9.9-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /service_pydj_user

ADD . /service_pydj_user

COPY ./package.txt /service_pydj_user/package.txt

COPY ./requirements.txt /service_pydj_user/requirements.txt

RUN pip install -r requirements.txt

RUN pip install -r package.txt

COPY . /service_pydj_user