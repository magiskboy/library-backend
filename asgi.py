import logging

from library import create_app

# disable uvicorn access log
logging.getLogger("uvicorn.access").handlers = []
logging.getLogger("uvicorn.access").propagate = False

app = create_app()
