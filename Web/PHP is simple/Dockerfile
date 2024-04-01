FROM php:7.4-cli-alpine

RUN mkdir -p /var/www/html/css

COPY app /var/www/html

WORKDIR /var/www/html

EXPOSE 9999

CMD ["php", "-S", "0.0.0.0:9999"]