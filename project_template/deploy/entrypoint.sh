#! /bin/bash

# Получить данные из файла с переменными окружения
export $(grep -v '^#' ./__env.env | xargs)

# Создать миграции
python ${NAME_PROJ}/manage.py makemigrations --no-input
# Применить миграции
python ${NAME_PROJ}/manage.py migrate --no-input

# Запустить сервер django
#python ${NAME_PROJ}/manage.py runserver 0.0.0.0:${EXTERNAL_WEB_PORT}

## Запустить сервер gunicorn
gunicorn --chdir ${NAME_PROJ} -c $(pwd)/deploy/gunicorn/gunicorn.conf.py