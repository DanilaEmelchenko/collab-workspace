from fastapi import APIRouter, Depends
from redis.asyncio import Redis
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.redis import get_redis
from app.db.session import get_session

router = APIRouter()


@router.get("")
async def health_check(
    db: AsyncSession = Depends(get_session),
    redis: Redis = Depends(get_redis),
) -> dict[str, str]:
    """Check health of all services."""
    # Check DB
    try:
        await db.execute(text("SELECT 1"))
        db_status = "ok"
    except Exception:
        db_status = "error"

    # Check Redis
    try:
        await redis.ping()
        redis_status = "ok"
    except Exception:
        redis_status = "error"

    return {
        "api": "ok",
        "database": db_status,
        "redis": redis_status,
    }
