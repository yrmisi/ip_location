from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .ip_cache import IPCache


class UserRequest(Base):
    """
    User query history.
    """

    __tablename__ = "user_requests"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        server_default=func.uuidv7(),
    )
    ip_queried: Mapped[str] = mapped_column(ForeignKey("ip_caches.ip"))
    user_agent: Mapped[str | None] = mapped_column(String(500))
    map_file_path: Mapped[str | None] = mapped_column(String(255))

    details: Mapped[IPCache] = relationship()
