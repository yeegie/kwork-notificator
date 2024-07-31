from abc import ABC, abstractmethod
from aiogram import Bot


class BaseNotificator(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    async def notify(self, bot: Bot, user_id: int, title: str, text: str) -> None:
        """
        Notify user by user_id

        @params:
            - user_id: int - user_id in telegram.
            - title: str - title for telegram message.
            - text: str - text for telegram message.
        """
        pass
