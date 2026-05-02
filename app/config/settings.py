from pydantic import BaseModel

from .database import DatabaseConfig
from .ip_info import IPInfoConfig
from .map import MapConfig


class Settings(BaseModel):
    ip_info: IPInfoConfig = IPInfoConfig()
    map: MapConfig = MapConfig()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()
