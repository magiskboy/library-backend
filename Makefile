all: start

deps-dev:
	@pip install -r requirements-dev.txt > /dev/null 2>&1

deps:
	@pip install -r requirements.txt > /dev/null 2>&1

dev: deps-dev
	@uvicorn --host 127.0.0.1 --port 5000 --reload --workers 1 --reload-dir library asgi:app

start: deps
	@gunicorn -c gunicorn.config.py asgi:app
