from abc import ABC, abstractmethod


class BaseDataBase(ABC):
    @staticmethod
    @abstractmethod
    async def connect():
        pass

    @staticmethod
    @abstractmethod
    async def close():
        pass
