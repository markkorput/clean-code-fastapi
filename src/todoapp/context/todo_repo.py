from ..entities.todo import Todo

class TodoRepo:
    def create(self, todo: Todo) -> Todo:
        ...

_todo_repo: TodoRepo | None = None

def get() -> TodoRepo:
    global _todo_repo
    assert _todo_repo
    return _todo_repo

def set(todo_repo: TodoRepo, force: bool = False):
    global _todo_repo
    
    if not force:
        assert not _todo_repo

    _todo_repo = todo_repo

