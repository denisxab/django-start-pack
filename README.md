# Начало

Скопировать(с заменой) данные шаблон в папку где хранятся стандартные шаблоны `Djnago` 

```bash
./venv/lib/python3.X/site-packages/django/conf/
```

Создать проект (`-e` указывает расширение файлов которые нужно отрендерить как шаблон)

```bash
django-admin startproject <ИмяПроекта> -e py,env,dockerignore,gitignore,yml,yaml,sh;
```

Создать приложение (`-e` указывает расширение файлов которые нужно отрендерить как шаблон)

```bash
django-admin startapp <ИмяПриложения> -e py,env,dockerignore,gitignore,yml,yaml,sh;
```
