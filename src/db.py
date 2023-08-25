import sqlalchemy as sa
from sqlalchemy.orm import registry, relationship

from src.domain import Task, TodoList

mapper_registry = registry()
metadata = mapper_registry.metadata

todo_lists = sa.Table(
    'todo_lists',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('name', sa.String(255), nullable=False),
)

tasks = sa.Table(
    'tasks',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('description', sa.String(255), nullable=False),
    sa.Column('is_done', sa.Boolean, nullable=False),
    sa.Column('todo_list_id', sa.Integer, sa.ForeignKey('todo_lists.id')),
)


def start_mappers():
    mapper_registry.map_imperatively(TodoList, todo_lists, properties={
        '_tasks': relationship(Task, backref='todo_list')
    })
    mapper_registry.map_imperatively(Task, tasks)

def create_tables(engine):
    metadata.create_all(engine)

def drop_tables(engine):
    metadata.drop_all(engine)

# get session for sqlitedb
def get_session():
    engine = sa.create_engine('sqlite:///todo.db')
    start_mappers()
    create_tables(engine)
    return sa.orm.sessionmaker(bind=engine)()

if __name__ == '__main__':
    engine = sa.create_engine('sqlite:///todo.db')
    start_mappers()
    create_tables(engine)