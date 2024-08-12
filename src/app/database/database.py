__all__ = ['DataBaseSQLite']

from .model import BaseDataBase
from tortoise import Tortoise

import os


class DataBaseSQLite(BaseDataBase):
    @staticmethod
    async def connect() -> None:
        db_path = 'database/'
        db_file = 'database.sqlite3'
        connection_string = f"sqlite://{db_path}{db_file}"

        if db_file not in os.listdir(db_path):
            with open(db_path + db_file, 'a'):
                os.utime(db_path + db_file, None)

        await Tortoise.init(
            db_url=connection_string,
            modules={'models': ['database.models']},
        )

        await Tortoise.generate_schemas()

    @staticmethod
    async def close() -> None:
        await Tortoise.close_connections()
