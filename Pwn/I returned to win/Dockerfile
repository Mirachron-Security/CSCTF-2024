FROM ubuntu:20.04

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY ./app/ /home/ctf/

RUN gcc -fno-stack-protector -z execstack -no-pie -m32 /home/ctf/main.c -o /home/ctf/main

RUN chmod +x /home/ctf/server.sh && \
    chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf 

EXPOSE 9999
USER ctf

CMD ["/home/ctf/server.sh"]
