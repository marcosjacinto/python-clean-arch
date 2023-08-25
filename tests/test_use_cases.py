import typing as t

import pytest

from src.domain import Task, TodoList
from src.use_cases import TodoListUseCase
from src.repository import TodoListRepositoryInterface


class FakeTodoListRepository(TodoListRepositoryInterface):

    def __init__(self, todo_lists: t.List[TodoList]=list()):
        self.todo_lists = todo_lists

    def get_todo_list_by_name(
            self, 
            todo_list_name: str
            ) -> t.Optional[TodoList]:
        
        for todo_list in self.todo_lists:
            if todo_list.name == todo_list_name:
                return todo_list
        return None
    
    def add_task(self, task: Task, todo_list_name: str):
        for todo_list in self.todo_lists:
            if todo_list.name == todo_list_name:
                todo_list.add_task(task)

    def add_todo_list(self, todo_list: TodoList):
        self.todo_lists.append(todo_list)
        

def test_get_task_from_todo_list_returns_none_if_not_found():
    todo_list_use_case= TodoListUseCase(
        todo_list_repository=FakeTodoListRepository()
    )
    assert todo_list_use_case.get_tasks(todo_list_name = 'mylist') == []

def test_get_task_from_todo_list_returns_task_if_found():

    todo_list = TodoList(1, name='mylist')
    todo_list2 = TodoList(2, name='mylist2')

    task1 = Task(title='mytask1', description='mydescription1', todo_list_id=1)
    task2 = Task(title='mytask2', description='mydescription2', todo_list_id=2)

    todo_list.add_task(task1)
    todo_list2.add_task(task2)

    todo_list_repo = FakeTodoListRepository(todo_lists=[todo_list, todo_list2])

    todo_list_use_case = TodoListUseCase(
        todo_list_repository=todo_list_repo
    )
    assert todo_list_use_case.get_tasks(todo_list_name = 'mylist') == [task1]

def test_add_task_to_todo_list():

    todo_list = TodoList(1, name='mylist')
    todo_list2 = TodoList(2, name='mylist2')

    task1 = Task(title='mytask1', description='mydescription1', todo_list_id=1)
    task2 = Task(title='mytask2', description='mydescription2', todo_list_id=2)

    todo_list.add_task(task1)
    todo_list2.add_task(task2)

    todo_list_repo = FakeTodoListRepository(todo_lists=[todo_list, todo_list2])

    todo_list_use_case = TodoListUseCase(
        todo_list_repository=todo_list_repo
    )

    task3 = Task(title='mytask3', description='mydescription3', todo_list_id=1)
    todo_list_use_case.add_task(task=task3, todo_list_name='mylist')
    assert todo_list_use_case.get_tasks(todo_list_name = 'mylist') == [task1, task3]

def test_add_task_to_todo_list_raises_error_if_id_doesnt_match():

    todo_list = TodoList(1, name='mylist')
    todo_list2 = TodoList(2, name='mylist2')

    task1 = Task(title='mytask1', description='mydescription1', todo_list_id=1)
    task2 = Task(title='mytask2', description='mydescription2', todo_list_id=2)

    todo_list.add_task(task1)
    todo_list2.add_task(task2)

    todo_list_repo = FakeTodoListRepository(todo_lists=[todo_list, todo_list2])

    todo_list_use_case = TodoListUseCase(
        todo_list_repository=todo_list_repo
    )

    task3 = Task(title='mytask3', description='mydescription3', todo_list_id=1)
    with pytest.raises(ValueError):
        todo_list_use_case.add_task(task=task3, todo_list_name='mylist2')