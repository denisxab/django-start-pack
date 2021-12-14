#! /bin/bash

# Создать миграции
python {{ project_name }}/manage.py makemigrations --no-input
# Применить миграции
python {{ project_name }}/manage.py migrate --no-input


# Запустить сервер django
python {{ project_name }}/manage.py runserver 0.0.0.0:8000

# Запустить сервер gunicorn
# gunicorn --chdir {{ project_name }} -c $(pwd)/deploy/gunicorn/gunicorn.conf.py