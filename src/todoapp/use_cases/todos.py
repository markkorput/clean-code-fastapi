from typing import Literal
from datetime import datetime
from dependency_injector.wiring import Provide, inject
from pydantic import BaseModel
from ..context.container import Container
from ..context.todo_repo import TodoRepo 
from ..entities.todo import Todo

class CreateTodoParams(BaseModel):
    user_id: str
    text: str
    done_at: datetime | None = None

@inject
def create_todo(params: CreateTodoParams, todos: TodoRepo = Provide[Container.todo_repo]) -> Todo:
    todo = Todo(user_id=params.user_id, text=params.text)
    todos.create(todo) 
    return todo

class UpdateTodoParams(BaseModel):
    text: str | None = None
    done_at: datetime | Literal[False] | None = None

@inject
def update_todo(todo_id: str, params: UpdateTodoParams, todos: TodoRepo = Provide[Container.todo_repo]) -> Todo:
    todo = todos.update(todo_id, params.model_dump(exclude_unset=True))
    return todo
