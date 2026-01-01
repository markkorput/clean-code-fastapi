from dependency_injector import containers, providers

from ..entities.todo import Todo

class TodoRepo:
    def create(self, todo: Todo) -> Todo:
        ...

class TodoRepoContainer(containers.DeclarativeContainer):
    todo_repo: TodoRepo = providers.Dependency()


