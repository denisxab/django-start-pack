# О чем этот проект

Этот репозиторий с шаблонами для быстрого создания `Django` проекта.

---

Настроены следующий набор технологий в шаблоне:

- `Django`
- `Docker`
- `Docker-compose`
- `Make`
- `Django Ninja`
- `PostgreSQL`
- `.env`
- `gunicorn`
- `Nginx`

В разработки:

- `React`

# Установка

Наша задача скопировать(с заменой) данные шаблон в папку где хранятся стандартные шаблоны `Djnago`.

---

Вот пример установки проекта, будем использовать виртуального окружения `venv`, и `Linux`.

```bash
# Создаем папку со всем проектом, И переходим в неё
dir="ИмяПроекта";
mkdir ${dir} && cd ${dir};
# Копируем этот репозиторий.
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
tree ./venv/lib/pythonn${py_version}/site-packages/django/conf/project_template &&
tree ./venv/lib/pythonn${py_version}/site-packages/django/conf/app_template 
```

# Использование

Создать проект (`-e` указывает расширение файлов которые нужно отрендерить как шаблон)

```bash
django-admin startproject <ИмяПроекта> -e py,env,dockerignore,gitignore;
```

Создать приложение (`-e` указывает расширение файлов которые нужно отрендерить как шаблон)

```bash
django-admin startapp <ИмяПриложения> -e py,env,dockerignore,gitignore;
```

# Особенности проекта

- Все настройки проекта хранят в файле с переменными окружениями `./__env.env`. Его нужно держать в тайне, так как в нём
  будут храниться приватные настройки для БД и `Django`.
- Для быстрого и удобного исполнения команд есть `./Makfile`. Для исполнения этого файла необходимо иметь
  программу `make`
  . На `Ubuntu` можно скачать эту программу командой `sudo apt install make`.
- Есть файл `./Dockerfile` для создания контейнера с проектом. `docker_build`  (Для правильной сборки образа и
  контейнера прочитайте `Makfile` в нем уже реализованы все необходимые настройки).
- Есть файл `./docker-compose.yml` для создания контейнера с БД. `docker_compose_up` (Для правильной сборки образа и
  контейнера прочитайте `Makfile` в нем уже реализованы все необходимые настройки).
- В папке `./deploy/gunicorn` хранятся настройки для запуска `gunicorn`, в этой же папке будут храниться логи.
- В папке `./<ИмяПроекта>/__cache` храниться кеш `Django`. Название этой папки определено
  настройками `settings.py->CACHES->"default"->"LOCATION"->"__cache"`
- В папке `db` будет храниться `volumes` для БД.

# Особенности приложения

...