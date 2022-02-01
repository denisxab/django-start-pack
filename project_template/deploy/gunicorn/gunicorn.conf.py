from os import path

from helpful import read_env_file_and_set_from_venv, isDev, getEnv

# УТОЧНЕНИЯ
# Путь к файлу с переменными окружениями
PATH_ENV = "/".join(__file__.split('/')[:-3])
# Чтение файла с переменными окружениями и добавление этих данных в ПО  `Python`
read_env_file_and_set_from_venv(path.join(PATH_ENV, "__env.env"))
# Слушать указанный ip адрес и порт  '<10.130.0.34:8001>'. Но лучше указать UDS сокет 'unix:/run/gunicorn.sock'
# bind = f"0.0.0.0:{getEnv('EXTERNAL_WEB_PORT')}"
bind = f"unix:{getEnv('WORK_DIR')}/deploy/gunicorn/gunicorn.sock"
print(bind)
# Путь к `WSGI` приложению  `ИмяГлавногоПриложения.wsgi:application`
wsgi_app = 'conf.wsgi:application'
ROOT_DIR = "/".join(__file__.split('/')[:-1])

# ПРОИЗВОДИТЕЛЬНОСТЬ
# Количество рабочих процессов для обработки запросов.
# Оптимально установить количество процессов по формуле `2-(4xЯдерЦпу)`
workers = 3
# Этот параметр используется для ограничения количества заголовков в запросе - предотвратить DDOS-атаку.
limit_request_fields = 32000
# Ограничьте допустимый размер поля заголовка HTTP-запроса.
limit_request_field_size = 0
# Максимальное количество одновременных клиентов
worker_connections = 1000

# ДРУГОЕ
# Авто перезагрузка сервера при изменении файлов проекта `Django`
reload = isDev()
# Путь для вывода лог данных
accesslog = f"{ROOT_DIR}/gunicorn_ass.log"  # !!! ПРОВЕРИТЬ ПУТИ ЛОГОВ
# Путь для вывода ошибок
errorlog = f"{ROOT_DIR}/gunicorn_err.log"  # !!! ПРОВЕРИТЬ ПУТИ ЛОГОВ
