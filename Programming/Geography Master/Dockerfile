FROM python:3.9-slim-buster

LABEL maintainer="Stratulat Dragos"

RUN /usr/sbin/useradd --no-create-home -u 1000 ctf 

WORKDIR /home/ctf

COPY app /home/ctf

RUN chown -R ctf:ctf /home/ctf && \
    chmod 750 /home/ctf /home/ctf/main.py && \
    pip install -r requirements.txt

EXPOSE 9999
USER ctf

CMD ["/usr/local/bin/python3", "-Bu", "/home/ctf/main.py", "> /home/ctf/out.log"]
