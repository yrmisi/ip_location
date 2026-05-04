from pathlib import Path

import folium
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.repositories import IPCacheRepository, UserRequestRepository


class MapService:
    """
    Service for generating and saving interactive HTML maps.
    """

    def __init__(
        self,
        ip: str,
        user_agent: str | None,
        session: AsyncSession,
    ) -> None:
        self.ip = ip
        self.user_agent = user_agent
        self.repo_ip_cache = IPCacheRepository(session)
        self.repo_request = UserRequestRepository(session)

    @property
    async def create_map(self) -> Path:
        """
        Generate a folium map, save it to disk, and log the user request.
        """
        location = await self.repo_ip_cache.get_location(self.ip)

        if location is None:
            raise ValueError
        m = folium.Map(
            location=location,
            zoom_start=12,
            tiles="CartoDB Voyager",
        )

        folium.Marker(
            location=location,
            tooltip="Click me!",
            popup="Point of interest",
            icon=folium.Icon(color="green"),
        ).add_to(m)

        file_path: Path = settings.map.file_path

        self.save_map(m, file_path)

        await self.repo_request.create_request(
            self.ip,
            self.user_agent,
            file_path.as_posix(),
        )
        return file_path

    @staticmethod
    def save_map(
        m: folium.Map,
        file_path: Path,
    ) -> None:
        """
        Add a custom favicon to the map and save it to the specified path.
        """
        root = m.get_root()
        header = getattr(root, "header", None)

        if header is not None:
            header.add_child(folium.Element(settings.map.favicon_html))

        m.save(file_path)
