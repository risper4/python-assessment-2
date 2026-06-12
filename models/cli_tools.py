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
        print(f"📌 Task '{project.title}' has been added to {self.name}'s project list")


# user1 = User('Maya', 'maya@gmail.com')
# user2 = User('James', 'james@gmail.com')
# user1.list_users()