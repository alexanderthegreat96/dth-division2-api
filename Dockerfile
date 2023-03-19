FROM python:3.12.0a3
FROM ultrafunk/undetected-chromedriver
RUN apt-get update && apt-get install -y locales

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip install --no-cache -r requirements.txt

COPY ./ .
