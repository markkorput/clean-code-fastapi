from dependency_injector.wiring import Provide, inject
from pydantic import BaseModel
from ..context.container import Container
from ..context.todo_repo import TodoRepo 
from ..entities.todo import Todo

class CreateTodoParams(BaseModel):
    user_id: str
    text: str

@inject
def create_todo(params: CreateTodoParams, todos: TodoRepo = Provide[Container.todo_repo]) -> Todo:
    todo = Todo(user_id=params.user_id, text=params.text)
    todos.create(todo) 
    return todo
