FROM python:3.6
ADD requirements /edx/app/registrar/requirements
ADD Makefile /edx/app/registrar
WORKDIR /edx/app/registrar
RUN make requirements
