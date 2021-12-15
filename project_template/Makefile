# Путь к переменным окружения
env_path=__env.env
include $(env_path)
export EXTERNAL_WEB_PORT, WORK_DIR, NAME_PROJ

## Переменные
# Имя контейнера БД
db_container_name:=$(NAME_PROJ)-postgres-db_cont
# Имя контейнера `nginx`
nginx_container_name:=${NAME_PROJ}-nginx_cont
# Имя контейнера `WEB`
web_container_name:=$(NAME_PROJ)-djnago-web_cont
# Имя образа `WEB`
image_name:=$(NAME_PROJ)_img
# Текущую директория
my_path=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
####


## Docker
# Получить ip адрес указанного контейнера
docker_get_ip:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(filter-out $@,$(MAKECMDGOALS));

# Получить ip адрес БД
docker_get_ip_db:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(db_container_name);

# Получить ip адрес WEB приложения
docker_get_ip_web:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(web_container_name);

# Создать образ проекта(Нудно находиться на одном уровне с `Dockerfile`)
docker_build:
	docker build --build-arg WORK_DIR=$(WORK_DIR) --build-arg NAME_PROJ=$(NAME_PROJ) -t $(image_name) .;

# Создать и запустить контейнер с проектом
docker_run:
	docker run --rm -ti --name $(web_container_name) -v $(my_path)/deploy:$(WORK_DIR)/deploy -p $(EXTERNAL_WEB_PORT):$(EXTERNAL_WEB_PORT) $(image_name);

# Подключиться к контейнеру c web
docker_exec_web:
	docker exec -ti $(web_container_name) /bin/sh;

# Подключиться к контейнеру c web
docker_exec_db:
	docker exec -ti $(db_container_name) /bin/sh;

# Подключиться к контейнеру c nginx
docker_exec_nginx:
	docker exec -ti $(nginx_container_name) /bin/sh;

# Подключиться к указанному контейнеру
docker_exec:
	docker exec -ti $(filter-out $@,$(MAKECMDGOALS)) /bin/sh;
####


## Docker-compose
# Запустить образы контейнеров
docker_compose_build:
	sudo docker-compose --env-file $(env_path) build;

# Запустить контейнеры а после окончанию отчистить удалить их
docker_compose_up:
	sudo docker-compose --env-file $(env_path) up && sudo docker-compose --env-file $(env_path) rm -fsv;

# Удалить ненужные контейнеры
docker_compose_rm:
	sudo docker-compose --env-file $(env_path) rm -fsv;
####


## Django
# Запустить сервер `django`
dj_run:
	python $(NAME_PROJ)/manage.py runserver 0.0.0.0:$(EXTERNAL_WEB_PORT);

# Запустить сервер `gunicorn` с конфигурацией  `gunicorn.conf.py`
dj_gunicorn_run:
	gunicorn --chdir $(NAME_PROJ) --preload -c $(my_path)/deploy/gunicorn/gunicorn.conf.py;

# Запустить тестовый сервер `gunicorn`
dj_gunicorn_run_test:
	gunicorn --chdir $(NAME_PROJ) --preload -b 0.0.0.0:$(EXTERNAL_WEB_PORT) --reload conf.wsgi:application;

# Создать миграции в БД
dj_migrate:
	python $(NAME_PROJ)/manage.py migrate && python $(NAME_PROJ)/manage.py flush;

# Загрузить данные в БД из дампа (позиционный аргумент - имя фала с дампом)
dj_load:
	python $(NAME_PROJ)/manage.py loaddata $(NAME_PROJ)/$(filter-out $@,$(MAKECMDGOALS));

# Создать дамб БД
dj_dump:
	python $(NAME_PROJ)/manage.py dumpdata > $(NAME_PROJ)/dump.json;

# Создать проект (позиционный аргумент - имя проекта)
dj_startproject:
	django-admin startproject $(filter-out $@,$(MAKECMDGOALS)); -e py,env,dockerignore,gitignore;