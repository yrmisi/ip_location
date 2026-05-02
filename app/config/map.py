import uuid
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel

from .paths import MAP_HTML_DIR


class MapConfig(BaseModel):
    prefix: str = "map"
    filename: str = f"{datetime.now().strftime('%Y%m%d')}_{uuid.uuid7()}.html"
    favicon_html: str = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🌐</text></svg>" />'

    @property
    def file_path(self) -> Path:
        return MAP_HTML_DIR / f"{self.prefix}_{self.filename}"
