FROM nginx:latest
MAINTAINER Tricster<mediosrity@qq.com>

RUN rm /usr/share/nginx/html/index.html

COPY ./default.conf /etc/nginx/conf.d/

COPY ./src/ /usr/share/nginx/html/

EXPOSE 80