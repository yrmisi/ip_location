from dataclasses import asdict

from fastapi import APIRouter, HTTPException, status
from requests.exceptions import HTTPError

from app.dependencies import AsyncSessionDep
from app.schemas import IPAddressRequest, IPInfo
from app.services import IPInfoService

router = APIRouter(
    tags=["ip info"],
)


@router.post("/ip_info")
async def create_ip_info(
    request: IPAddressRequest,
    session: AsyncSessionDep,
) -> dict[str, str | float]:
    """
    Fetch geolocation data for a specific IP and store it in the database.
    """
    try:
        ip_info_service: IPInfoService = IPInfoService(request.ip_address, session)
        ip_info: IPInfo = await ip_info_service.get_info_ip()
        return asdict(ip_info)
    except HTTPError as exc:
        print(f"HTTP error occurred: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve IP information from external service: {exc.response.status_code} {exc.response.text}",
        )
    except Exception as exc:
        print(f"Other error occurred: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {exc}",
        )
