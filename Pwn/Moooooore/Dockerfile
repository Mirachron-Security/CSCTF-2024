FROM ubuntu:16.04

RUN dpkg --add-architecture i386 && \
    apt-get update -y && apt-get install -y \
        gcc nano socat libc6-dev-i386 libc6:i386

RUN /usr/sbin/useradd --no-create-home -u 1000 ctf

WORKDIR /home/ctf

RUN cp -R /lib* /home/ctf && \
    cp -R /usr/lib* /home/ctf

COPY ./app/ /home/ctf/

RUN gcc -fno-stack-protector -z execstack -no-pie -m32 /home/ctf/main.c -o /home/ctf/main

RUN chmod +x /home/ctf/server.sh && \
    chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    chmod 740 /home/ctf/flag.txt

EXPOSE 9999
USER ctf

CMD ["/home/ctf/server.sh"]
