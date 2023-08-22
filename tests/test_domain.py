from src.domain import Task, TodoList

def test_task_is_created_with_correct_attributes():
    task = Task('title', 'description')
    assert task.title == 'title'
    assert task.description == 'description'
    assert task.is_done == False

def test_set_task_as_done():
    task = Task('title', 'description')
    task.set_as_done()
    assert task.is_done == True

def test_set_task_as_undone():
    task = Task('title', 'description')
    task.set_as_done()
    task.set_as_undone()
    assert task.is_done == False

def test_create_empty_todo_list():
    todo_list = TodoList()
    assert todo_list.tasks == []

def test_create_todo_list_with_tasks():
    task1 = Task('title1', 'description1')
    task2 = Task('title2', 'description2')
    todo_list = TodoList([task1, task2])
    assert todo_list.tasks == [task1, task2]

def test_add_task_to_todo_list():
    task = Task('title', 'description')
    todo_list = TodoList()
    todo_list.add_task(task)
    assert todo_list.tasks == [task]

def test_remove_task_from_todo_list():
    task = Task('title', 'description')
    todo_list = TodoList([task])
    todo_list.remove_task(task)
    assert todo_list.tasks == []

def test_get_task_from_todo_list():
    task = Task('title', 'description')
    todo_list = TodoList([task])
    assert todo_list.get_task('title') == task

def test_get_task_from_todo_list_returns_none_if_not_found():
    task = Task('title', 'description')
    todo_list = TodoList([task])
    assert todo_list.get_task('not found') == None    
