FROM python:3.9-slim-buster

ENV FLAG='CSCTF{3xeCUTE_c0mm@nds_w1th_dec3r32lized_PIckles}'

RUN /usr/sbin/useradd --no-create-home -u 1000 ctf 

WORKDIR /home/ctf

COPY app /home/ctf

RUN chown -R root:ctf /home/ctf && \
    chmod 750 /home/ctf /home/ctf/main.py && \
    pip install -r requirements.txt

EXPOSE 9999

USER ctf

CMD ["/usr/local/bin/python3", "-Bu", "/home/ctf/main.py", "> /home/ctf/out.log"]
