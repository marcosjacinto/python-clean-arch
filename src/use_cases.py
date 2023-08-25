from src.repository import TodoListRepositoryInterface
from src.domain import Task, TodoList


class TodoListUseCase():

    def get_tasks(self, todo_list_name: str):
        return []