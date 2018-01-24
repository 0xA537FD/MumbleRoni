FROM debian:stretch-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       git \
       python-dev \
       python3-pip

RUN mkdir /etc/mumbleroni
WORKDIR /etc/mumbleroni

RUN git config --global http.sslVerify false \
    && git clone --recurse-submodules https://github.com/Peter-Morawski/MumbleRoni.git .

RUN apt-get install -y --no-install-recommends \
       libav-tools \
       opus-tools

RUN pip3 install setuptools \
    && pip3 install wheel \
    && pip3 install -r requirements.txt \
    && pip3 install -r pymumble/requirements.txt

VOLUME ["/etc/mumbleroni/config", "/etc/mumbleroni/mumbleroni/modules"]

CMD ["python3", "run.py"]