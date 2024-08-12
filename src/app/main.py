from config import Settings
from container import container
from notificator import Notificator
from parser import Parser
from database import DataBaseSQLite

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

import asyncio
import time

# TEMP
from parser import KworkCategory


async def main():
    bot = Bot(
        token=Settings().telegram.token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        )
    )

    parser = Parser(category=KworkCategory.SCRIPTS_AND_BOTS)
    notificator = Notificator(bot)
    database = DataBaseSQLite()

    await database.connect()

    # Dependency registration
    container.register('bot', bot)
    container.register('parser', parser)
    container.register('notificator', notificator)
    container.register('database', database)

    await parser.parse_all()


if __name__ == "__main__":
    asyncio.run(main())
