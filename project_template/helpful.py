from os import getenv, environ
from re import sub
from pprint import pprint

IS_READ_ENV_FILE: bool = False

FILE_NAME_ENV: str = "./__env.env"


def isDev() -> bool:
    """
    Это режим отладки ?
    """
    return True if getEnv("DEBUG") == 'true' else False


def getEnv(name_env: str) -> str:
    """
    Если мы не читали файл с конфигурациями, то читаем его,
    а после этого переопределяем функцию
    """
    if not IS_READ_ENV_FILE:
        raise FileExistsError("Вы не прочитали файл с переменными окружения")
    #  Переопределение функции без проверки
    return getenv(name_env)


def read_env_file_and_set_from_venv(file_name: str = FILE_NAME_ENV):
    """
    Чтение переменных окружения из указанного файла, и добавление их в ПО `python`
    """
    global IS_READ_ENV_FILE
    with open(file_name, 'r', encoding='utf-8') as _file:
        res = {}
        for line in _file:
            tmp = sub(r'^#[\s\w\d\W\t]*|[\t\s]', '', line)
            if tmp:
                k, v = tmp.split('=', 1)
                # Если значение заключено в двойные кавычки, то нужно эти кавычки убрать
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]

                res[k] = v
    environ.update(res)
    pprint(res)
    IS_READ_ENV_FILE = True
