from typing import Any
from dataclasses import replace
import pytest
from dependency_injector import providers
from todoapp.entities.todo import Todo
from todoapp.context.container import Container
from todoapp.context.todo_repo import TodoRepo

class InMemoryTodoRepo(TodoRepo):
    def __init__(self):
        self.todos: list[Todo] = []

    def create(self, todo):
        ids = sorted(t.id or "" for t in self.todos)
        todo.id = str(int(ids[-1]) + 1) if len(ids) else 1
        self.todos.append(todo) 
        return todo

    def update(self, id: str, values: dict[str, Any]):
        todo: Todo = next(t for t in self.todos if t.id == id)
        todo = replace(todo, **values)
        self.todos = [todo if t.id == todo.id else t for t in self.todos]
        return todo

@pytest.fixture
def todo_repo():
    return InMemoryTodoRepo()

@pytest.fixture(autouse=True)
def _inject_test_repo(todo_repo: InMemoryTodoRepo):
    container = providers.Container(Container, todo_repo=todo_repo)
    container.wire() # packages=["todoapp.use_cases"])
