from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import UserRequest


class UserRequestRepository:
    """Repository for managing user request history."""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_request(
        self,
        ip_address: str,
        user_agent: str | None = None,
        map_file_path: str | None = None,
    ) -> None:
        """
        Records a new user request in the database.
        """
        user_request = UserRequest(
            ip_queried=ip_address,
            user_agent=user_agent,
            map_file_path=map_file_path,
        )
        self.session.add(user_request)
        await self.session.commit()
