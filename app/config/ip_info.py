from pydantic import BaseModel


class IPInfoConfig(BaseModel):
    """
    Configuration for external IP geolocation API.
    """

    url: str = "http://ip-api.com/json/{ip}"
