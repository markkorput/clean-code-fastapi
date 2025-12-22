from todoapp.use_cases.todos import create_todo, CreateTodoParams
from todoapp.context.todo_repo import TodoRepo, set

class InMemoryTodoRepo(TodoRepo):
    def __init__(self):
        self.todos = []

    def create(self, todo):
        ids = sorted(t.id for t in self.todos)
        todo.id = ids[-1] + 1 if len(ids) else 1
        self.todos.append(todo) 
        return todo

class TestCreateTodo:
    def test_adds_new_todo_to_repo(self):
        todos = InMemoryTodoRepo()
        params = CreateTodoParams(user_id="test", text="TEST")
        todo = create_todo(params, todos=todos)
        assert todo.id
        assert todo.text == params.text
        assert todo.user_id == params.user_id
        assert todos.todos == [todo]
