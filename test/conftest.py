import pytest
from dependency_injector import providers
from todoapp.context.container import Container
from todoapp.context.todo_repo import TodoRepo

class InMemoryTodoRepo(TodoRepo):
    def __init__(self):
        self.todos = []

    def create(self, todo):
        ids = sorted(t.id for t in self.todos)
        todo.id = ids[-1] + 1 if len(ids) else 1
        self.todos.append(todo) 
        return todo

@pytest.fixture
def todo_repo():
    return InMemoryTodoRepo()

@pytest.fixture(autouse=True)
def _inject_test_repo(todo_repo: InMemoryTodoRepo):
    container = providers.Container(Container, todo_repo=todo_repo)
    container.wire() # packages=["todoapp.use_cases"])
