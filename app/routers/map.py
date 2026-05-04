from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Header, HTTPException, status
from fastapi.responses import FileResponse

from app.dependencies import AsyncSessionDep
from app.services import MapService

router = APIRouter(
    tags=["get map"],
)


@router.get("/map")
async def get_map(
    ip: str,
    session: AsyncSessionDep,
    user_agent: Annotated[str | None, Header()] = None,
) -> FileResponse:
    """
    Generate an interactive map for the given IP and return it as a file.
    """
    try:
        map_service: MapService = MapService(ip, user_agent, session)
        file_path: Path = await map_service.create_map
        return FileResponse(file_path)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate map: {exc}",
        )
