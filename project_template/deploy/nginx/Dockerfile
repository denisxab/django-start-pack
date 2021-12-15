# Беерм образ `nginx`
FROM nginx:alpine
# Удяляем стандарный конфиг
RUN rm /etc/nginx/conf.d/default.conf
# Копируем шаблон в контейнер
COPY default.conf.template /etc/nginx/templates/default.conf.template
