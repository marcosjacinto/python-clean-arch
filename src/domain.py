import typing as t
from dataclasses import dataclass, field

@dataclass
class Task:
    title: str
    description: str
    is_done: bool = False
    todo_list_id: t.Optional[int] = None

    def set_as_done(self):
        self.is_done = True

    def set_as_undone(self):
        self.is_done = False

@dataclass
class TodoList:
    id: int
    name: str = 'default'
    tasks: t.List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task: Task):
        self.tasks.remove(task)

    def get_task(self, title: str):
        for task in self.tasks:
            if task.title == title:
                return task
        return None