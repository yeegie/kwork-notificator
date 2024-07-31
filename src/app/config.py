__all__ = ['Settings']

from configparser import ConfigParser
from pydantic_settings import BaseSettings
from pydantic import BaseModel

parser = ConfigParser()
parser.read(r'config.ini')


class TelegramConfig(BaseModel):
    _section = "Telegram"

    token: str = parser.get(_section, "token")
    recipient: int = parser.getint(_section, "recipient")


class Settings(BaseSettings):
    telegram: TelegramConfig = TelegramConfig()
