import pytest
from dependency_injector import providers
from todoapp.use_cases.todos import create_todo, CreateTodoParams
from todoapp.context.todo_repo import TodoRepo, TodoRepoContainer

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
    container = providers.Container(TodoRepoContainer, todo_repo=todo_repo)
    container.wire(modules=[__name__])

class TestCreateTodo:
    def test_adds_new_todo_to_repo(self, todo_repo):
        params = CreateTodoParams(user_id="test", text="TEST")
        todo = create_todo(params) 
        assert todo.id
        assert todo.text == params.text
        assert todo.user_id == params.user_id
        assert todo_repo.todos == [todo]
