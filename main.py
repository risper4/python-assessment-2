# Imports json feature
import json

# import json file
data_file = 'data.json'

import os

import argparse
# Imported classes from cli_classes
from models.cli_classes import User, Task, Project

# Uses info dict
users = {}

def add_user(args) :    # Adds user as an object and to users{}
   if args.user in users :
       print('❌ User already exists in the program')
       return
   else :
       user = User(args.user, args.email)
       users[args.user] = user
       print(f"User '{args.user}' has been added successfully")
    
def add_project(args) :    # Adds new project
    user = users.get(args.user)
    if not user :
        print("❌ User not found")
        return
    project = Project(args.title , args.due_date)
    for prj in user.projects :
        if prj.title == project.title :
            print(f"Project '{project.title}' is already in the project list")
        else :
            user.add_project(project)
    

def list_users(args) :   # Lists all users
    if not User.users_list:
        print('❌ Users currently not found')
        return
    else :
        print('These are the current users : ')
        for user in User.users_list :
            print(f"- {user.name} ({user.email})")
    

def add_task(args) :    # Adds new task
    user = users.get(args.user)

    target_project = [project for project in user.projects if project.title == args.project_title]

    if target_project :
        task = Task(args.task_title)
        target_project.add_task(task)
        return
    else :
        print("❌ Project not found")

def mark_complete(args) :    # Marks a specifc task complete
    user = users.get(args.user)

    if user :
        current_project = [project for project in user.project if args.project_title == project.title]
        if current_project :
            for task in current_project.task :
                if args.task_title == task.title :
                    task.complete()
                    return
                else :
                    print('❌ Task not found')
        else :
            print('❌ Project not found')
    else :
        print('❌ User not found')


def save_data() :
    data = {}      # Stores user info in the json file

    for name, user in users.items() :   # Uses name to access the user's objects info
        data[name] = {
            'name' : user.name,
            'email' : user.email,
            'projects' : [     # List comprehension to loop over project object
                {
                    'title' : project.title,
                    'due-date' : project.due_date,
                    'tasks' : [{'title' : project.task, 'complete' : project.complete} for task in project.tasks]  # List comprehension to loop over task object
                }
                for project in user.projects
                ]
        }

    with open(data_file, 'w') as file :    # Writes the data in the data.json file
        json.dump(data, file, indent=4)
    print('Data successfully saved')
        

         
def main() :
    parser = argparse.ArgumentParser(description='Project Management Tool') 
    subparsers = parser.add_subparsers() 
    
    # Subparser for adding users
    add_user_parser = subparsers.add_parser("add-user" , help="Adds new user")
    add_user_parser.add_argument("--user", required=True)
    add_user_parser.add_argument("--email", required=True)
    add_user_parser.set_defaults(func=add_user)

    # Subparser for listing users
    user_parser = subparsers.add_parser("list-user" , help="Displays all users")
    user_parser.set_defaults(func=list_users)

    # Subparser for adding projects  
    add_project_parser = subparsers.add_parser("add-project" , help="Adds a new project to the user's list")
    add_project_parser.add_argument("--user", required=True)
    add_project_parser.add_argument("--project_title", required=True)
    add_project_parser.add_argument("--due_date", required=True)
    add_project_parser.set_defaults(func=add_project)
    
    # Subparser for adding tasks
    add_task_parser = subparsers.add_parser("add-task" , help="Adds a new task to the user's projects")
    add_task_parser.add_argument("--user", required=True)
    add_task_parser.add_argument("--project_title", required=True)
    add_task_parser.add_argument("--task_title", required=True)
    add_task_parser.set_defaults(func=add_task)

    #Subparser that marks a task complete
    complete_parser = subparsers.add_parser("mark-complete" , help='Marks tasks complete')
    complete_parser.add_argument("--user", required=True)
    complete_parser.add_argument("--project_title", required=True)
    complete_parser.add_argument("--task_title" , required=True)
    complete_parser.set_defaults(func=mark_complete)

    #Implements cli commands
    args = parser.parse_args()
    if hasattr(args, "func") :
        args.func(args)
    else :
        parser.print_help()

    save_data()   # Saves data after every command

    
if __name__ == "__main__":
    main()



