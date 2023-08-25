import typing as t
from abc import ABC, abstractmethod

import sqlalchemy as sa

from src.domain import Task, TodoList


class TodoListRepositoryInterface(ABC):

    @abstractmethod
    def get_todo_list_by_name(
        self, 
        todo_list_name: str
        ) -> t.Optional[TodoList]:
        pass

    @abstractmethod
    def add_task(self, task: Task, todo_list_name: str):
        pass

    @abstractmethod
    def add_todo_list(self, todo_list: TodoList):
        pass

class SQLTodoListRepository(TodoListRepositoryInterface):
    
    def __init__(self, session: sa.orm.Session):
        self.session = session

    def get_todo_list_by_name(
            self, 
            todo_list_name: str
            ) -> t.Optional[TodoList]:
        todo_list = self.session.query(
            TodoList
            ).filter_by(name=todo_list_name).first()
        
        return todo_list
    
    def add_todo_list(self, todo_list: TodoList):
        self.session.add(todo_list)
        self.session.commit() 

    def add_task(self, task: Task, todo_list_name: str):
        todo_list = self.get_todo_list_by_name(todo_list_name)
        task.todo_list_id = todo_list.id
        self.session.add(task)
        self.session.commit()
