# О чем этот проект

Этот репозиторий с шаблонами для быстрого создания `Django` проекта.

---

В шаблоне проекта настроены следующий технологий:

- `Django`
- `gunicorn` (В качестве `WSGI` сервера)
- `Django Ninja` (В качестве `REST API`)
- `Docker`
- `Docker-compose`
- `Nginx` (Через `Docker-compose`)
- `PostgreSQL` (Через `Docker-compose`)
- `.env` (Все важные настройки проекта хранятся в переменных окружения)
- `Makefile` (Готовые стандартные команды для работы с проектом)
- `npm`
- `React` (Для рендеринга шаблонов)
- `webpack.config.js` (Для автоматической сборки `React` при изменении файлов)
- `.gitignore` && `.dockerignore`
- Логирование `loguru`
- `poetry`

# Установка

Наша задача скопировать(с заменой) данные шаблон в папку где хранятся стандартные шаблоны `Djnago`.

---

Вот пример замены стандартных шаблонов `Django` на наши, будем использовать виртуальное окружение `venv`, и `Linux`. (
Этот скрипт можно выполнить за одну команду).

```bash
# Создаем папку со всем проектом, И переходим в неё
dir="NameProj";
mkdir ${dir} && cd ${dir};
# Копируем этот репозиторий.a
git clone https://github.com/denisxab/django-start-pack.git .;
# На всякий случай выходим из ВО если мы в нем находимся.
deactivate;
# Создаем виртуальное окружение, Актируем его, устанавливаем `Django`.
python -m venv venv && . ./venv/bin/activate && pip install Django;
# Создаем переменную с версий текущего ВО `Python`.
py_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))');
# Удаляем стандартные шаблон проекта и приложения `Django`.
rm -rf ./venv/lib/python${py_version}/site-packages/django/conf/project_template ./venv/lib/python${py_version}/site-packages/django/conf/app_template;
# Копируем шаблоны из репозитория в ВО.
cp -r project_template ./venv/lib/python${py_version}/site-packages/django/conf/ &&
cp -r app_template ./venv/lib/python${py_version}/site-packages/django/conf/ &&
# Удаляем ненужные файлы/папки.
rm -rf project_template app_template .git;
# Показать результат `Django` шаблона
tree ./venv/lib/python${py_version}/site-packages/django/conf/project_template &&
tree ./venv/lib/python${py_version}/site-packages/django/conf/app_template;
```

# Использование

Создать проект (`-e` указывает расширение файлов которые нужно отрендерить как шаблон)

```bash
django-admin startproject <ИмяПроекта> -e py,env,dockerignore,gitignore,json --template ./venv/lib/python${py_version}/site-packages/django/conf/project_template;
```

Создать приложение (`-e` указывает расширение файлов которые нужно отрендерить как шаблон)

```bash
django-admin startapp <ИмяПриложения> -e py,env,dockerignore,gitignore,json --template ./venv/lib/python${py_version}/site-packages/django/conf/app_template;
```

---

Настроим и запустим проект.

```bash
cd <ИмяПроекта>;
# Первоначально настраиваем проект
make init_proj;
# Запуска `webpack`
make webpack_run;
# Запускам `Django` сервер (запустите в новом окне)
make dj_run;
```

> И теперь можно начинать разрабатывать свой проект, не задумываться о первоначальных настройках.

# Особенности созданного проекта через этот шаблон

- Общее

    - Файл с переменными окружения называется `__env.env`
    - Все настройки проекта хранят в файле с переменными окружения `./__env.env`. Его нужно держать в тайне, так как в
      нём будут храниться приватные настройки для БД и `Django`. Он уже занесен в `.gitignore`
    - Для быстрого и удобного исполнения команд есть `./Makfile`. Для исполнения этого файла необходимо иметь
      программу `make`
      . На `Ubuntu` можно скачать эту программу командой `sudo apt install make`.
    - Для `poetry` в шаблоне `pyproject.toml` нужно указать имя проекта в ручную, так как он (более логично) находится
      выше проекта, и поэтому не обрабатывается шаблонизатором  `Django`

- `Django`

    - Главное приложение теперь имеет название `conf`
    - Кеш `Django` хранятся по пути `./<ИмяПроекта>/__cache.*`
    - Логи `Django` хранятся по пути `./deploy/log_django/*`

- `Docker`

    - Есть файл `./Dockerfile` для создания контейнера с проектом. `make docker_build` - собрать образ (Для правильной
      сборки образа и контейнера прочитайте `Makfile` в нем уже реализованы все необходимые настройки).
    - Есть файл `./docker-compose.yml` для создания контейнера с `PostgreSQL` и `nginx`. `make docker_compose_up` -
      запустить контейнеры (Для правильной сборки образа и контейнера прочитайте `Makfile` в нем уже реализованы все
      необходимые настройки).
    - В папке `./deploy/gunicorn` хранятся настройки для запуска `gunicorn`, в этой же папке будут храниться логи
      от `gunicorn`.
    - `gunicorn` в `Docker` настроен прослушивать `Unix Socket` по пути `./deploy/gunicorn/gunicorn.sock`, поэтому
      правильно запускать сервер через `Docker-compose` в котором настроен `Nginx`.
    - В папке `db` будет храниться `volumes`(термин из `Docker`) для БД.

- `React`

    - В качестве шаблонизатор будем использовать `React` который храниться в приложение `frontend_react`. Главный
      компонент
      `React` находиться по пути `./ИмяПроекта/frontend_react/src/App.js`
    - Скомпилированный код `webpack` храниться по
      пути `./ИмяПроекта/frontend_react/static/frontend_react/public/main.js`

# Особенности созданного приложения через этот шаблон

- Есть папки `static`, `templates`, `templatetags`
- Есть предварительные шаблоны для моделей и админ панели
