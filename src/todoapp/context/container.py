
from dependency_injector import containers, providers
from .todo_repo import TodoRepo

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["todoapp.use_cases"],
        auto_wire=False
    )

    todo_repo: TodoRepo = providers.Dependency()

