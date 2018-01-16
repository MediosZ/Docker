FROM python:latest
MAINTAINER Tricster<mediosrity@qq.com>

COPY ./hello.py /back/

RUN pip install hug pymongo --upgrade

EXPOSE 80

ENTRYPOINT [ "hug", "-p", "80", "-f", "/back/hello.py" ]