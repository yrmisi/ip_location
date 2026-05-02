from datetime import datetime, timezone

from sqlalchemy import DateTime, Float, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class IPCache(Base):
    """
    Cache IP information to avoid API fees/limits.
    """

    __tablename__ = "ip_caches"

    ip: Mapped[str] = mapped_column(
        String(45),
        primary_key=True,
        index=True,
    )
    country: Mapped[str] = mapped_column(String(100))
    region: Mapped[str] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(100))
    zip: Mapped[str] = mapped_column(String(50))
    lat: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        index=True,
    )
    lon: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        index=True,
    )
    timezone: Mapped[str] = mapped_column(String(100))
    isp: Mapped[str] = mapped_column(String(100))
    raw_data: Mapped[str] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        nullable=False,
    )
