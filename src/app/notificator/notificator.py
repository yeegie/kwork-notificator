from .model import BaseNotificator
from aiogram import Bot


class Notificator(BaseNotificator):
    """
    ### Class for sending notifications to one or more recipients 🔔
    """

    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    async def notify(self, user_id: int, title: str, text: str) -> None:
        """
        Notify user by user_id

        Send message to user. A bot will not be able to send a message to a user who has not started a dialogue.

        @params:
            - user_id: int - user_id in telegram.
            - title: str - title for telegram message.
            - text: str - text for telegram message.
        """
        try:
            await self._bot.send_message(
                chat_id=user_id,
                text=f"<b>{title}</b>\n\n{text}",
            )
        except Exception as ex:
            pass
