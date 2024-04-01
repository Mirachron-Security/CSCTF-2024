FROM php:7.4-cli-alpine


RUN apk update && apk add dcron sudo

RUN adduser -D ctf && adduser -D scriptuser

COPY app/ /var/www/html/
RUN chown -R ctf:ctf /var/www/html && \
    chmod -R 755 /var/www/html && \
    mkdir -p /var/www/html/uploads && \
    chown ctf:ctf /var/www/html/uploads

COPY create/ /var/www/scripts/
RUN chown -R root:scriptuser /var/www/scripts && \
    chmod 750 /var/www/scripts/*

USER ctf

WORKDIR /var/www/html

EXPOSE 9999

USER root
ENTRYPOINT ["/var/www/scripts/entrypoint.sh"]
