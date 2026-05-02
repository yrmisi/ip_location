from dataclasses import dataclass


@dataclass
class IPInfo:
    country: str
    region: str
    city: str
    zip: str
    lat: float
    lon: float
    timezone: str
    isp: str

    def __str__(self) -> str:
        return f"""
        Country: {self.country}
        Region: {self.region}
        City: {self.city}
        Zip: {self.zip}
        Lat: {self.lat}
        Lon: {self.lon}
        Timezone: {self.timezone}
        ISP: {self.isp}
        """
