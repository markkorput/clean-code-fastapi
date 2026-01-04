from todoapp.use_cases.todos import create_todo, CreateTodoParams

class TestCreateTodo:
    def test_adds_new_todo_to_repo(self, todo_repo):
        params = CreateTodoParams(user_id="test", text="TEST")

        assert todo_repo.todos == []
        todo = create_todo(params) 
        assert todo.id
        assert todo.text == params.text
        assert todo.user_id == params.user_id
        assert todo_repo.todos == [todo]
        
