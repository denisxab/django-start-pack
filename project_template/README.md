# Начало

Скопировать(с заменой) данные шаблон в папку

```bash
./venv/lib/python3.9/site-packages/django/conf/
```

# Django

Создать проект (`-e` указывает разширение файлов котрые нужно отренедерить как шаблон)

```bash
django-admin startproject <ИмяПроекта> -e py,env,dockerignore,gitignore,yml,yaml,sh;
```

Создать приложение

```bash

```

# Docker

Создать образ проекта(Нудно находиться на одном уровне с `Dockerfile`)

```bash
docker build --build-arg WORK_DIR=/usr/src/<ИмяПроекта>  -t <ИмяОбразаПроекта> .;
```

Создать и запустить контейнер с проектом

```bash
docker run --rm -ti  --name <ИмяКонтейнераПроекта> -p 8080:8000 <ИмяОбразаПроекта> ;
```

Подключиться к контейнеру

```bash
docker exec -ti  <ИмяКонтейнераПроекта> /bin/sh
```

# Docker-compose
