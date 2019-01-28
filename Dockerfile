FROM python:3.6
ADD requirements /edx/app/registrar/registrar/requirements
ADD Makefile /edx/app/registrar/registrar
WORKDIR /edx/app/registrar/registrar
RUN make requirements
ADD . /edx/app/registrar/registrar
EXPOSE 16616
