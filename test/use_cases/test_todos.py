from datetime import datetime
from todoapp.entities.todo import Todo
from todoapp.use_cases.todos import create_todo, update_todo, CreateTodoParams, UpdateTodoParams
from ..conftest import InMemoryTodoRepo

class TestCreateTodo:
    def test_adds_new_todo_to_repo(self, todo_repo: InMemoryTodoRepo):
        params = CreateTodoParams(user_id="test", text="TEST")

        assert todo_repo.todos == []
        todo = create_todo(params) 
        assert todo.id
        assert todo.text == params.text
        assert todo.user_id == params.user_id
        assert todo.done_at is None
        assert todo_repo.todos == [todo]


class TestUpdateTodo:
    def test_patches_existing_todo_in_repo(self, todo_repo: InMemoryTodoRepo):
        todo = todo_repo.create(Todo(text="Initial Text", user_id="1", done_at=datetime.now()))
        params = UpdateTodoParams(text="New Text", done_at=None)
        updated_todo = update_todo(todo.id, params)
        assert updated_todo != todo
        assert updated_todo.id == todo.id
        assert updated_todo.text == params.text
        assert updated_todo.done_at is None
        assert todo_repo.todos == [updated_todo]

