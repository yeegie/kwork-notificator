from abc import ABC, abstractmethod


class BaseObserver(ABC):
    @abstractmethod
    def update(self, subject: "BaseSubject") -> None:
        pass


class BaseSubject(ABC):
    @abstractmethod
    async def attach(self, observer: BaseObserver) -> None:
        pass

    @abstractmethod
    async def detach(self, observer: BaseObserver) -> None:
        pass

    @abstractmethod
    async def notify(self) -> None:
        pass
