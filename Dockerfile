FROM python:3

ENV PYTHONIOENCODING UTF-8
ENV TZ=Asia/Bishkek

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc//timezone

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir static && mkdir media
COPY . .

RUN python3 manage.py collectstatic --noinput

RUN chmod -R 755 /usr/src/app/static

EXPOSE 8000