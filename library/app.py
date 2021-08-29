import asyncpg
from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from library import apis, db
from library.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title="Library",
        version="0.1.0",
        default_response_class=UJSONResponse,
        debug=settings.debug,
    )

    @app.on_event("startup")
    async def startup():
        db.pool = await asyncpg.create_pool(
            host=settings.db_host,
            port=settings.db_port,
            user=settings.db_username,
            password=settings.db_pass,
            database=settings.db_name,
        )

    @app.on_event("shutdown")
    async def shutdown():
        if db.pool:
            await db.pool.close()

    apis.init_app(app)

    return app
