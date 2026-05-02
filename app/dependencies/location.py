from typing import Annotated

from fastapi import Depends

from app.schemas import LocationRequest

LocationDep = Annotated[LocationRequest, Depends()]
