FROM python:3

#copia os instant client
COPY instantclient_basic.rpm ./
COPY instantclient_devel.rpm ./

#instala programas necessÃ¡rios para instalaÃ§Ã£o
RUN apt-get update
RUN apt-get -y install rpm alien libaio1 

#instala o instant client
RUN alien instantclient_basic.rpm 
RUN alien instantclient_devel.rpm
RUN dpkg -i oracle-instantclient12.2-basic_12.2.0.1.0-2_amd64.deb
RUN dpkg -i oracle-instantclient12.2-devel_12.2.0.1.0-2_amd64.deb

#cria variÃ¡veis de ambiente para o oracle
ENV ORACLE_HOME=/usr/lib/oracle/12.2/client64
ENV LD_LIBRARY_PATH=/usr/lib/oracle/12.2/client64/lib

#vai para o diretÃ³rio da app
WORKDIR /usr/src/app

#copia os requisitos do python e instala em um ambiente virtual
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#copia todo o projeto
COPY . .

CMD [ "python", "./app.py" ]