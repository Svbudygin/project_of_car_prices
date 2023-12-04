# сначала мы указываем, какой образ питона для проекта мы берём
FROM python:3.11-bullseye

# копируем файл с зависимостями внутрь будущего контейнера
COPY ./requirements.txt /app/requirements.txt

# переключаемся внутри контейнера на свежесобранную папку app/
WORKDIR /app

# устанавливаем зависимости 
RUN pip install -r requirements.txt

# копируем всё остальное
COPY . /app

# скажем контейнеру бежать от лица питона
ENTRYPOINT [ "python3" ]

# запускаем
CMD [ "app.py" ]

# (по факту команда для запуска == "python3 app.py")
