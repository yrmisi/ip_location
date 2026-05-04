from typing import Any

import httpx
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.repositories import IPCacheRepository
from app.schemas import IPInfo


class IPInfoService:
    def __init__(
        self,
        ip_address: str,
        session: AsyncSession,
    ) -> None:
        self.ip = ip_address
        self.url = settings.ip_info.url
        self.repo = IPCacheRepository(session)

    async def get_info_ip(self) -> IPInfo:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(self.url.format(ip=self.ip))
            response.raise_for_status()
            data: dict[str, Any] = response.json()

        ip_info: IPInfo = IPInfo(
            country=data.get("country", "Unknown"),
            region=data.get("regionName", "Unknown"),
            city=data.get("city", "Unknown"),
            zip=data.get("zip", "Unknown"),
            lat=float(data.get("lat", 0.0)),
            lon=float(data.get("lon", 0.0)),
            timezone=data.get("timezone", "Unknown"),
            isp=data.get("isp", "Unknown"),
        )
        await self.repo.create_or_update_ip_cache(self.ip, ip_info, str(data))
        return ip_info
