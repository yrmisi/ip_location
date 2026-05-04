from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import IPCache
from app.schemas import IPInfo


class IPCacheRepository:
    """ """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_or_update_ip_cache(
        self,
        ip_address: str,
        ip_data: IPInfo,
        raw_json: str,
    ) -> None:
        """ """
        result = await self.session.execute(select(IPCache).where(IPCache.ip == ip_address))
        ip_cache: IPCache | None = result.scalar_one_or_none()

        if ip_cache:
            ip_cache.lat = ip_data.lat
            ip_cache.lon = ip_data.lon
            ip_cache.city = ip_data.city
            ip_cache.raw_data = raw_json
        else:
            ip_cache = IPCache(
                ip=ip_address,
                country=ip_data.country,
                region=ip_data.region,
                city=ip_data.city,
                zip=ip_data.zip,
                lat=ip_data.lat,
                lon=ip_data.lon,
                timezone=ip_data.timezone,
                isp=ip_data.isp,
                raw_data=raw_json,
            )
            self.session.add(ip_cache)

        await self.session.commit()

    async def get_location(self, ip_address: str) -> list[float] | None:
        """ """
        stmt = select(IPCache.lat, IPCache.lon).where(IPCache.ip == ip_address)
        result = await self.session.execute(stmt)
        row = result.one_or_none()

        if row:
            return [row.lat, row.lon]
        return None
