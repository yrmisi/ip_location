from pydantic import BaseModel


class IPAddressRequest(BaseModel):
    ip_address: str
