from config import Settings
from container import container
from notificator import Notificator

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

import asyncio


async def startup():
    notificator: Notificator = container.resolve('notificator')
    await notificator.notify(
        user_id=423420323,
        title="Test Notify 🔔",
        text="Hello, World!",
    )


def main():
    bot = Bot(
        token=Settings().telegram.token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        )
    )

    # parser = Parser()
    notificator = Notificator(bot)

    # Dependency registration
    container.register('bot', bot)
    # container.register('parser', parser)
    container.register('notificator', notificator)

    asyncio.run(startup())


if __name__ == "__main__":
    main()
