__all__ = ['KworkOrder', 'KworkCategory', 'BaseParser']

from abc import ABC, abstractmethod
from typing import Tuple
from pydantic import BaseModel, HttpUrl
from datetime import datetime
from enum import IntEnum


class KworkOrder(BaseModel):
    title: str
    description: str
    price: int
    time_left: datetime
    offers: int
    hired: int
    url: HttpUrl


class KworkCategory(IntEnum):
    SCRIPTS_AND_BOTS = 41
    WEBSITES_CREATION = 37


class BaseParser(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def parse_all(self, category) -> Tuple[KworkOrder]:
        """
        ### Parse kwork exchange

        @params:
            - category: KworkCategory

        @returns:
            - Tuple[KworkOrder]
        ---
        @example:
        result = parser.parse(category=KworkCategory.SCRIPTS_AND_BOTS)
        """
        pass


    @abstractmethod
    def add_param(self, key: str, value: str):
        pass


    @abstractmethod
    def add_param(self, key: str, value: str):
        pass
