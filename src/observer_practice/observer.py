from typing import Protocol

class Observer(Protocol):
    def actualizar(self, mensaje):
        ...