FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
WORKDIR /app

RUN apt-get update \
  && apt-get install python3-dev default-libmysqlclient-dev gcc -y

RUN pip install --upgrade pip  
RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry install

COPY . /app/

EXPOSE 8000  

RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["sh","/app/docker-entrypoint.sh"]
