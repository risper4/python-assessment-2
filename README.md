# Project Management CLI Tool

### By Risper Gichia

## Introduction

* A command line interface that manages companies internal :
    - Users
    - Projects
    - Tasks
* Where each user is assigned a project, where each project has its own tasks assigned to individual user.

* The command line tool runs on `main.py`.


## Instructions

* These are the step-by-step instructions on how to use the Task Management Tool :
    
    1. Adding users
- Run on terminal : `python3 main.py add-user --user '*name*' --email '*email*'`
    2. Listing present users
- Run on terminal : `python3 main.py list-user`
    3. Adding projects to a specific user
-  Run on terminal : `python3 main.py add-project --user '*name*' --project_title '*title*' --project_due_date '*due_date*'`
    4. Adding task to a user's assigned project
- Run on terminal : `python3 main.py add-task --user '*name*' --project_title '*title*' --task_title '*title*'`

* For any assistance :
- `python3 main.py --help`


## Tools used
  - Python (mainly)
  - Rich (extarnal dependancy)
  - json file


## Bugs
* The program does not have a fully developed and effective json file for data persistance


### Access
* Access the program through :
    * Github : `https://github.com/risper4/python-assessment-2.git`


#### Contact
    * Github : `risper4`