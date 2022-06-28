FROM python:3.8.13-alpine3.15

ENV PYTHONUNBUFFERED=0

COPY . .

RUN pip install -r requirements.txt

RUN crontab crontab

CMD ["crond", "-f"]