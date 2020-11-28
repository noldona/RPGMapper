FROM python:3.6
LABEL maintainer="Ron Jones <noldona@gmail.com>"

WORKDIR /api
COPY . /api
RUN pip install -r requirements.txt

CMD ["uwsgi", "api.ini"]
