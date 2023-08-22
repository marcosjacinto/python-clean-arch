import typing as t
from dataclasses import dataclass

@dataclass
class Task:
    title: str
    description: str
    is_done: bool = False

    def set_as_done(self):
        self.is_done = True