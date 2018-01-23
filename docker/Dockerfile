FROM debian:stretch-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       git \
       python-dev \
       python-pip

RUN mkdir /etc/mumbleroni
WORKDIR /etc/mumbleroni

RUN git config --global http.sslVerify false \
    && git clone --recurse-submodules https://github.com/Peter-Morawski/MumbleRoni.git

RUN add-apt-repository ppa:kirillshkrogalev/ffmpeg-next \
    && apt-get update \
    && apt-get install ffmpeg \
    && apt-get install opus-tools

RUN pip install setuptools \
    && pip install wheel \
    && pip install -r requirements.txt

CMD ["python", "run.py"]