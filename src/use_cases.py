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
    
    def add_task(self, task: Task, todo_list_name: str):
        todo_list = self.todo_list_repository.get_todo_list_by_name(todo_list_name)
        if todo_list.id != task.todo_list_id:
            raise ValueError('ID of task and todo_list must be the same')
        self.todo_list_repository.add_task(task, todo_list.name)
