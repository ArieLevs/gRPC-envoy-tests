FROM python:3.7-alpine

MAINTAINER Arie Lev

ENV PYTHONUNBUFFERED 1
ARG PYPI_REPO="https://pypi.python.org/simple"
ENV PYPI_REPO $PYPI_REPO

RUN apk add --update --no-cache \
    gcc \
    linux-headers \
    make \
    musl-dev \
    python-dev \
    g++

RUN mkdir /messenger
ADD messenger/requirements.txt .

RUN pip install --upgrade pip

RUN pip install \
    --index-url $PYPI_REPO \
    --requirement requirements.txt

ADD messenger /messenger
WORKDIR /messenger

# Generate gRPC classes
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. messenger.proto

RUN apk del g++ make musl-dev python-dev

# Cleanup
ENV PYPI_REPO 'None'

CMD ["echo", "override command to start server/client"]
