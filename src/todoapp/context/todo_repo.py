from typing import Any
from abc import abstractmethod
from ..entities.todo import Todo

class TodoRepo:
    @abstractmethod
    def create(self, todo: Todo) -> Todo:
        ...

    @abstractmethod
    def update(self, id: str, values: dict[str, Any]) -> Todo:
        ...
