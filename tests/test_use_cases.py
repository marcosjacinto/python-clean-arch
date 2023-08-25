import typing as t

from src.domain import Task, TodoList
from src.use_cases import TodoListUseCase


def test_get_task_from_todo_list_returns_none_if_not_found():
    todo_list = TodoListUseCase()
    assert todo_list.get_tasks(todo_list_name = 'mylist') == []