import re

class User :
    users_list = []   # Stores all users
    def __init__(self, name, email):
        self._name = name
        self._email = email
        self.projects = []     # Stores all projects to a certain user
        User.users_list.append(self)

    @property   # User name getter
    def name(self) :
        return self._name
    
    @name.setter    # User name setter
    def name(self,value) :
        if not isinstance(value, str) or len(value) < 1 :
            raise ValueError('Error : Name should be a string')
        else :
            self._name = value

    @property      # User email getter
    def email(self) :   
        return self._email
    
    @email.setter    # User email setter
    def email(self, value) :
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", value):
            raise ValueError('Error : Email should be in the right format')

    def list_users(self) :    # Lists all user name
        print(f'These are the all users : ')
        for user in User.users_list :
            print(f'{user.name}')

    def add_project(self, project) :    # Adds a project to the user's list
        self.projects.append(project)
        print(f"📌 Project '{project.title}' has been added to {self.name}'s project list")


class Project :
    project_list = []    # Stores all projects
    def __init__(self, title, due_date):
        self._title = title
        self._due_date = due_date
        self.tasks = []    # Stores all tasks to a specific project
        Project.project_list.append(self)

    @property     # Project title getter
    def title(self) :   
        return self._title
    
    @title.setter     # Project title setter
    def title(self,value) :
        if len(value) < 1 or not isinstance(value, str):
            raise ValueError('Error : Project title should be a string')
        else :
            self._title = value

    @property     # Project due_date getter
    def due_date(self) :
        return self._due_date
    
    @due_date.setter    # Project due_date setter
    def due_date(self, value) :
        if re.match(r'(\d{2})/(\d{2})/(\d{4})', value) :
            raise ValueError('Error : Date should be in DD/MM/YYYY format')
        else :
            self._due_date = value

    def add_task(self, task) :    # Adds a new task to the project's to-do list
        self.tasks.append(task)
        print(f" 📌 Task '{task.title}' is added to {self.title}'s to-do list")


class Task :
    def __init__(self, title):
        self._title = title
        self.complete = False

    @property     # Task title getter
    def title(self) :
        return self._title
    
    @title.setter
    def title(self,value) :     # Task title setter
        if len(value) < 1 or not isinstance(value, str):
            raise ValueError('Error : Task title should be a string')
        else :
            self.title = value

    def mark_complete(self) :    # Marks a specified task as complete
        self.complete = True
        print(f" ✅ Task '{self.title}' is marked complete")


# user1 = User('Maya', 'maya@gmail.com')
# user2 = User('James', 'james@gmail.com')
# project1 = Project('Research', '23/3/2026')
# user1.list_users()
# user1.add_project(project1)