### Уточнения
import os
import re
from pprint import pprint


def read_env_file_and_set_from_venv(file_name: str):
	"""Чтение переменных окружения из указанного файла, и добавление их в ПО `python`"""
	with open(file_name, 'r', encoding='utf-8') as _file:
		res = {}
		for line in _file:
			tmp = re.sub(r'^#[\s\w\d\W\t]*|[\t\s]', '', line)
			if tmp:
				k, v = tmp.split('=', 1)
				# Если значение заключено в двойные кавычки, то нужно эти кавычки убрать
				if v.startswith('"') and v.endswith('"'):
					v = v[1:-1]
				
				res[k] = v
	os.environ.update(res)
	pprint(res)

# Путь к файлу с переменными окружениями
PATH_ENV = "/".join(__file__.split('/')[:-3])
# Чтение файла с перемеными окружениями и добавлени этих данных в ПО  `Python`
read_env_file_and_set_from_venv(os.path.join(PATH_ENV, "__env.env"))
# Слушать указанный ip адрес и порт  '<10.130.0.34:8001>'. Но лучше указать UDS сокет 'unix:/run/gunicorn.sock'
bind = f"127.0.0.1:{os.environ.get('EXTERNAL_WEB_PORT')}"
# Путь к `WSGI` приложению  `ИмяГлавногоПриложения.wsgi:application`
wsgi_app = f"{os.environ.get('NAME_PROJ')}.wsgi:application"
ROOT_DIR = "/".join(__file__.split('/')[:-1])

### Производительность
# Количество рабочих процессов для обработки запросов. Оптимально установить количество процессов по формуле `2-(4xЯдерЦпу)`
workers = 3
# Этот параметр используется для ограничения количества заголовков в запросе до предотвратить DDOS-атаку.
limit_request_fields = 32000
# Ограничьте допустимый размер поля заголовка HTTP-запроса.
limit_request_field_size = 0
# Максимальное количество одновременных клиентов
worker_connections = 1000

### Другие
# Авто перезагрузка сервера при изменении файлов проекта `Django`
reload = True
# Путь для вывода лог данных
accesslog = f"{ROOT_DIR}/gunicorn_ass.log"  # !!! ПРОВЕРИТЬ ПУТИ ЛОГОВ
# Путь для вывода ошибок
errorlog = f"{ROOT_DIR}/gunicorn_err.log"  # !!! ПРОВЕРИТЬ ПУТИ ЛОГОВ
