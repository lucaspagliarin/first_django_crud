# Listagem de Pessoas

First CRUD using Django

- What is CRUD?
>  CRUD é a sigla pra Create, Read, Update e Delete.
  São funções importantes para manipulação de dados em banco de dados.

- Why DJANGO?
>  Achei Django uma maneira facil e rápida de implementar aplicações WEB. Depois de anos distante da programação, achei uma maneira facil de recomeçar e praticar minhas habilidades de programação

## Inicializando a Aplicação
- pipenv install django
- pipenv shell (preferencialmente dentro do vscode)
- django-admin startproject PROJECT_NAME .
- python manage.py runserver
- python manage.py migrate 
- python manage.py createsuperuser

## Criando Aplicativos

- python manage.py startapp core
- adicionar 'core' no settings.py
- adicionar url no urls.py
- criar views
- criar templates

## Models

Models são representações do Banco de Dados. Cada Model representa uma tabela no DB, seus atributos são as colunas.
>  from django.db import models
>  models.Model 

- Adicionar o Model no admin.py
> admin.site.register(Model)

- Gerar Migrations
>    python manage.py makemigration
>    python manage.py migrate

- Funções do Objeto Model
> https://docs.djangoproject.com/en/4.1/topics/db/queries/