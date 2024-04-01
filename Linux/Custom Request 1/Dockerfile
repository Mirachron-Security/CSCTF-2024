FROM python:3.9-slim-buster

RUN /usr/sbin/useradd --no-create-home -u 1000 ctf 

WORKDIR /home/ctf

COPY app /home/ctf

RUN chown -R ctf:ctf /home/ctf && \
    chmod 755 /home/ctf && \
    chmod 750 /home/ctf/main.py && \
    pip install -r requirements.txt && \
    touch /home/ctf/requests.log && \
    chown ctf:ctf /home/ctf/requests.log && \
    chmod 640 /home/ctf/requests.log

EXPOSE 9999
USER ctf

CMD ["/usr/local/bin/python3", "-Bu", "/home/ctf/main.py", "> /home/ctf/out.log"]
