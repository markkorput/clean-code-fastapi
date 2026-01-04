from abc import abstractmethod
from ..entities.todo import Todo

class TodoRepo:
    @abstractmethod
    def create(self, todo: Todo) -> Todo:
        ...

