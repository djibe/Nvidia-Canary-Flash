FROM pytorch/pytorch:latest
# python:3

LABEL version="0.1" maintainer="djibe"

WORKDIR /app

COPY . /app/

RUN apt-get update && \
  apt-get install -y git &&\
  pip install pybind11 &&\
  pip install wheel setuptools pip --upgrade &&\
  pip install fasttext-wheel &&\
  pip install --no-cache-dir -r requirements.txt && \
  pip install && \
  pip install git+https://github.com/NVIDIA/NeMo.git@r1.23.0#egg=nemo_toolkit[asr]

CMD [ "python", "./app.py" ]
