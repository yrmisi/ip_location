from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from app.database import async_engine
from app.routers import health_router, ip_router, map_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Lifespan for the application."""
    yield

    await async_engine.dispose()


app = FastAPI(title="IP info", lifespan=lifespan)

app.include_router(ip_router, prefix="/api")
app.include_router(map_router, prefix="/api")
app.include_router(health_router)
