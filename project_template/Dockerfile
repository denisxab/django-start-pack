 # Взять за основу образ `python` `alpine` самый легковестный `Linux`
FROM python:3.9

# Получем аргумент из `docker-compose.yml` (путь рабочей деректории)
ARG WORK_DIR
ARG NAME_PROJ
# Отобразить путь к консоле дабы убедиться в существавание Аргумента
RUN echo $WORK_DIR $NAME_PROJ
# Создать робочую деректроию проекта ( Обычно путь такой `/usr/src/<ИмяПрограммы>`)
WORKDIR $WORK_DIR

ENV \
    # Не создавать папку `.pyc` для кеширование байт кода
    PYTHONDONTWRITEBYTECODE=1 \
    # Не кешировать вывод из консоли
    PYTHONUNBUFFERED=1

###  ПРОВЕРИТь КОПИРОВАНИЕ ФАЙЛОВ В КОНТЕЙНЕР
# ЯВНО Скопировать файл зависимости в рабочую деректроию
COPY ${NAME_PROJ}/requirements.txt ${WORK_DIR}/requirements.txt
# ЯВНО Скопировать исполняемый скрипт
COPY deploy/entrypoint.sh ${WORK_DIR}/deploy/entrypoint.sh
# Скопировать весь проект в робочию дерикторию
COPY . .

RUN \
    # Обновить `pip`
    pip install --upgrade pip;\
    # Установить зависемости из файла
    pip install -r ${NAME_PROJ}/requirements.txt; \
    # Разрешить исполнять файл
    chmod +x deploy/entrypoint.sh; \
    # Отчистить кеш `apt`
    rm -rf /var/lib/apt/lists/*;

# Выполнить скрипт при запуске контейнера
ENTRYPOINT sh deploy/entrypoint.sh