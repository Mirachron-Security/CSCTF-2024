FROM php:8.0.3-cli-alpine

RUN mkdir -p /var/www/html

COPY app /var/www/html

WORKDIR /var/www/html

EXPOSE 9999

CMD ["php", "-S", "0.0.0.0:9999"]
