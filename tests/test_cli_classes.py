import pytest

from models.cli_classes import User, Project, Task

@pytest.fixture(autouse=True)
def reset_class_lists() :
    User.users_list = []
    Project.project_list = []
    yield

def test_add_user() :
    user = User('Dave', 'dave@gmail.com')
    assert user.name == 'Dave'
    assert user.email == 'dave@gmail.com'

def test_added_user_to_users_list() :
    user = User('Dave', 'dave@gmail.com')
    assert user in User.users_list
    assert len(User.users_list) == 1

def test_start_with_empty_projects() :
    user = User('Dave', 'dave@gmail.com')
    assert user.projects == []

def test_add_project() :
    user = User('Dave', 'dave@gmail.com')
    project = Project('Portfolio', '23/3/2026')
    user.add_project(project)

    assert project in user.projects
    assert len(user.projects) == 1



def test_add_project() :
    project = Project('Portfolio', '23/3/2026')
    assert project.title == 'Portfolio'
    assert project.due_date == '23/3/2026'

def test_added_project_to_project_list() :
    project = Project('Portfolio', '23/3/2026')
    assert project in Project.project_list

def test_start_with_empty_task() :
    project = Project('Portfolio', '23/3/2026')
    assert project.tasks == []

def test_add_task() :
    project = Project('Portfolio', '23/3/2026')
    task = Task('UX design')
    project.add_task(task)

    assert task in project.tasks
    assert len(project.tasks) == 1

def test_add_task() :
    task = Task('UX design')
    assert task.title == 'UX design'
    assert task.complete == False

def test_task_complete() :
    task = Task('UX design')
    task.mark_complete()
    assert task.complete == True