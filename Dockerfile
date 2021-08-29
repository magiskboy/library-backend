FROM python:3.8-alpine3.12

LABEL maintainer="nguyenkhacthanh244@gmail.com" version="0.0.1"

WORKDIR /app

RUN apk update --no-cache && \
    apk add --no-cache make gcc g++ musl-dev

ADD ./requirements.txt .

RUN python -mvenv venv && \
    venv/bin/pip install cython && \
    venv/bin/pip install -r requirements.txt

FROM python:3.8-alpine3.12

WORKDIR /app

COPY --from=0 /app/venv ./venv

ADD . .

EXPOSE 80

ENTRYPOINT ./venv/bin/gunicorn -c gunicorn.config.py asgi:app

CMD /bin/sh
