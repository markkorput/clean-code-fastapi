from fastapi import Depends
from pydantic import BaseModel
from ..context import todo_repo
from ..entities.todo import Todo

class CreateTodoParams(BaseModel):
    user_id: str
    text: str

def create_todo(params: CreateTodoParams, todos = Depends(todo_repo.get)) -> Todo:
    todo = Todo(user_id=params.user_id, text=params.text)
    todos.create(todo) 
    return todo
