FROM php:7.4-cli-alpine

RUN mkdir -p /var/www/html/files/images; \
    mkdir /var/www/html/files/flags

COPY app /var/www/html

WORKDIR /var/www/html

EXPOSE 9999

CMD ["php", "-S", "0.0.0.0:9999"]
