FROM python:3.8-slim  

ENV ENTRYPOINT_DEFAULT_DATABASE_URI ${ENTRYPOINT_DEFAULT_DATABASE_URI}

RUN apt-get update \
    && apt-get install -y --no-install-recommends postgresql-client \
        procps \
        build-essential \
        git \
        wait-for-it \
    && mkdir /code 

WORKDIR /code/ 
ADD . /code/ 

# install requirements
RUN pip install -U pip \
    && pip install -r requirements.txt \
    && chmod +x /code/docker-entrypoint.sh

EXPOSE 8000