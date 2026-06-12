class User :
    users_list = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects = []
        User.users_list.append(self)

    def list_users(self) :
        print(f'These are the all users : ')
        for user in User.users_list :
            print(f'{user.name}')
    
    def add_project(self, project) :
        self.projects.append(project)
        print(f"📌 Project '{project.title}' has been added to {self.name}'s project list")


class Project :
    project_list = []
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.tasks = []
        Project.project_list.append(self)

    def add_task(self, task) :
        self.tasks.append(task)
        print(f" 📌 Task '{task.title}' is added to {self.title}'s to-do list")





# user1 = User('Maya', 'maya@gmail.com')
# user2 = User('James', 'james@gmail.com')
# project1 = Project('Research', '23/3/2026')
# user1.list_users()
# user1.add_project(project1)