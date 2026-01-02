from ..entities.todo import Todo

class TodoRepo:
    def create(self, todo: Todo) -> Todo:
        ...

