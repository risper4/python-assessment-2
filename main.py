import argparse

from models.cli_classes import User, Task, Project

users = {}
def add_user(args) :
    user = User(args.user, args.email)
    users[args.user] = user
    
def add_project(args) :
    user = users.get(args.user)
    if not user :
        print("❌ User not found")
        return
    project = Project(args.title , args.due_date)
    for prj in user.projects :
        if prj.title == project.title :
            print(f"Project '{project.title}' is already in the project list")
        else :
            user.add_task(project)
    

def list_user(args) :
    user = users.get(args.user)
    if user :
        user.list_users()
    else :
        print("❌ No users found")

def add_task(args) :
    user = users.get(args.user)

    target_project = [project for project in user.projects if project.title == args.project_title]

    if target_project :
        task = Task(args.task_title)
        target_project.add_task(task)
    else :
        print("❌ Project not found")

         
    
        

