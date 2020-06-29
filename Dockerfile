# Base Image
FROM ubuntu:18.04
FROM python:3.7.3-stretch

ENV PYTHONUNBUFFERED 1

# General Packages
RUN apt-get update \
    && apt-get install -y software-properties-common \
    && apt-get install -y build-essential \
    && apt-get install -y python-dev \
    && apt-get install -y python-pip \
    && apt-get install -y python3-pip \
    && apt-get update \
    && apt-get install -y default-libmysqlclient-dev \
    && apt-get install -y git

# Set locale
ENV LC_ALL=C.UTF-8

# Upgrading pip
RUN python -m pip install pip --upgrade
RUN apt-get update

# Setup Folders
RUN mkdir -p /TestProject

# Move to working directory
WORKDIR /TestProject

# Add working directory
COPY . /TestProject

# Setup requirements
RUN cd /TestProject \
    && pip3 install -r requirements.txt

# Open Port for the Python App
EXPOSE 8000
