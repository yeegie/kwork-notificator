__all__ = ['container']

class Container:
    def __init__(self):
        self._services = {}

    def register(self, key: str, service):
        self._services[key] = service

    def resolve(self, key: str):
        return self._services.get(key)


container = Container()
