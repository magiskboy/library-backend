from fastapi import APIRouter

from library import db

router = APIRouter(prefix="/health")


@router.get("/")
async def health_check():
    async with db.pool.acquire(timeout=10) as connection:
        async with connection.transaction():
            result = await connection.fetchval("select 42")
    if result:
        return result
    return "Hello world"
