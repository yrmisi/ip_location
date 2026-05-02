from pydantic import BaseModel


class IPInfoConfig(BaseModel):
    url: str = "http://ip-api.com/json/{ip}"
