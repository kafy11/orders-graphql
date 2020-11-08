FROM python:3

#vai para o diretÃ³rio da app
WORKDIR /usr/src/app

#copia os requisitos do python e instala em um ambiente virtual
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#copia todo o projeto
COPY . .

RUN python create_db.py

CMD [ "python", "./app.py" ]