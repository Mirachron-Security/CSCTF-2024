FROM chronospkk/chronos-ubuntu-mysql:20.04

EXPOSE 9999

RUN mkdir -p /app
WORKDIR /app

COPY app/docker_run_mysql.sh /app
COPY app/start.sql /app
COPY app/main.py /app/main.py
COPY app/generate_flag.py /app
COPY app/requirements.txt /app

RUN chmod +x /app/docker_run_mysql.sh && \
    pip3 install -r requirements.txt

CMD ["/app/docker_run_mysql.sh"]
