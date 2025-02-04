from functools import wraps
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis.asyncio import Redis, ConnectionPool
from src.core.config import settings
from circuitbreaker import circuit

def cache(expire: int = 60):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await FastAPICache.get_backend().wrap(
                func, 
                key=f"{func.__name__}:{str(args)}:{str(kwargs)}",
                expire=expire
            )(args, kwargs)
        return wrapper
    return decorator 

pool = ConnectionPool.from_url(
    str(settings.redis_url),
    max_connections=100,
    socket_timeout=1,
    retry_on_timeout=True
)

class CacheService:
    def __init__(self):
        self.redis = Redis(connection_pool=pool)

    @circuit(failure_threshold=5, recovery_timeout=30)
    async def get(self, key: str):
        return await self.redis.get(key)

    @circuit(failure_threshold=5, recovery_timeout=30)
    async def set(self, key: str, value: str, ttl: int = 60):
        return await self.redis.setex(key, ttl, value) 