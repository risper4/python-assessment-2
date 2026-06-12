class User :
    users_list = []   # Stores all users
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects = []     # Stores all projects to a certain user
        User.users_list.append(self)

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
        self.title = title
        self.due_date = due_date
        self.tasks = []    # Stores all tasks to a specific project
        Project.project_list.append(self)

    def add_task(self, task) :    # Adds a new task to the project's to-do list
        self.tasks.append(task)
        print(f" 📌 Task '{task.title}' is added to {self.title}'s to-do list")


class Task :
    def __init__(self, title):
        self.title = title
        self.complete : False

    def add_task(self) :    # Marks the specified task as complete
        self.complete = True
        print(f" ✅ Task '{self.title}' is marked complete")


# user1 = User('Maya', 'maya@gmail.com')
# user2 = User('James', 'james@gmail.com')
# project1 = Project('Research', '23/3/2026')
# user1.list_users()
# user1.add_project(project1)