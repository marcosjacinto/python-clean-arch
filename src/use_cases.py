from src.repository import TodoListRepositoryInterface
from src.domain import Task, TodoList


class TodoListUseCase():

    def __init__(self, todo_list_repository: TodoListRepositoryInterface) -> None:
        self.todo_list_repository = todo_list_repository

    def get_tasks(self, todo_list_name: str):
        todo_list = self.todo_list_repository.get_todo_list_by_name(todo_list_name)
        if todo_list is None:
            return []
        return todo_list.tasks
    