from src.domain import Task

def test_task_is_created_with_correct_attributes():
    task = Task('title', 'description')
    assert task.title == 'title'
    assert task.description == 'description'
    assert task.is_done == False

def test_set_task_as_done():
    task = Task('title', 'description')
    task.set_as_done()
    assert task.is_done == True

