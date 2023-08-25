import typing as t
from abc import ABC, abstractmethod

from src.domain import Task, TodoList


class TodoListRepositoryInterface(ABC):

    @abstractmethod
    def get_todo_list_by_name(self, todo_list_name: str) -> t.Optional[TodoList]:
        pass

    @abstractmethod
    def add_task(self, task: Task, todo_list_name: str):
        pass

    @abstractmethod
    def add_todo_list(self, todo_list: TodoList):
        pass
