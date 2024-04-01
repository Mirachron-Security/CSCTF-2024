FROM ubuntu:20.04

LABEL maintainer="chronos@chronossec.site"

ENV TZ=Europe/Bucharest
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt-get install -y --no-install-recommends \
    python3 pip mysql-server net-tools nano wget curl less && apt-get clean
RUN pip install mysql-connector-python

