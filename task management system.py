

import easygui

tasks = {
    
    "T1": {
        
        "TITLE": "Design Homepage",
        "DESCRIPTION": "Create a mockup of the homepage",
        "ASSIGNEE": ["JSM"],
        "PRIORITY": "3",
        "STATUS": "In progress",
        
    },
    
    "T2": {
        
        "TITLE": "Implement Login page",
        "DESCRIPTION": "Create the Login page for the website",
        "ASSIGNEE": ["JSM"],
        "PRIORITY": "3",
        "STATUS": "Blocked",
        
    },
    
    "T3": {
        
        "TITLE": "Fix navigation",
        "DESCRIPTION": "Fix tha navigation menu to be more user-friendly",
        "ASSIGNEE": None,
        "PRIORITY": "1",
        "STATUS": "Not started",
        
    },
    
    "T4": {
        
        "TITLE": "Add payment processing",
        "DESCRIPTION": "Implement payment processing for the website",
        "ASSIGNEE": ["JLO"],
        "PRIORITY": "",
        "STATUS": "In progress",
        
    },
    
    "T5": {
        
        "TITLE": "Create an About Us page",
        "DESCRIPTION": "Create a page with information about the company",
        "ASSIGNEE": ["BDI"],
        "PRIORITY": "1",
        "STATUS": "Blocked",
        
    },
    
}

team_members = {
    
    "JSM": {
        
        "Name": "John Smith",
        "Email": "John@techvision.com",
        "Tasks assigned": [tasks["T1"], tasks["T2"]]
        
    },
    
    "JLO": {
        
        "Name": "Jane Love",
        "Email": "Jane@techvision.com",
        "Tasks assigned": [tasks["T4"]]
        
    },
    
    "BDI": {
        
        "Name": "Bob Dillon",
        "Email": "Bob@techvision.com",
        "Tasks assigned": [tasks["T5"]]
        
    },
    
}


def question(given_string, options):
    response = easygui.buttonbox(given_string, choices=options)
    return response

def show_all():
    
    final_str = f""
    
    for task_id in tasks:
        final_str += f"\n\n{task_id}: \n\n"
        for task_id_values in tasks[task_id]:
            final_str += f"{task_id_values}: {tasks[task_id][task_id_values]}\n"
            
    easygui.msgbox(final_str)
    
def add_task():
    
    task_number = 1
    for task_number in range(len(tasks)):
        task_number += 1
    
    tasks[f"T{task_number}"] = {}
    
    possible_assignee = []
    
    
    for possible_member in team_members:
        possible_assignee.append(f"{possible_member} ({team_members[possible_member]['Name']})")

        
    new_task_values = [["Give a title for this new task: ", "TITLE", None], 
                       ["Give a description for this new task: ", "DESCRIPTION", None],
                       ["Add people to work on this task", "ASSIGNEE", possible_assignee],
                       ["From 1-3, how important is this task?", "PRIORITY"],
                       ["Choose a status for this task", "STATUS", 
                        ["In progress", "Not started", "Blocked"]]]
        
    for i in range(len(new_task_values)):
        if new_task_values[i][1] == "ASSIGNEE":
            chosen_member = ""
            already_looped = False
            while chosen_member != "(Stop adding members)" or chosen_member != None:
                print("asdasd")
    
    

options = {
    
    "See project progress report":{
        
        "FUNCTION": show_all,
        "PARAMETERS": {},
        
    },
    
    "Add new task":{
        
        "FUNCTION": add_task,
        "PARAMETERS": {},
        
    }
    
}

given_options = []
for options_functions in options:
    given_options.append(options_functions)

users_choice = question("What would you like to do?", given_options)

for functions in options:
    if functions == users_choice:
        if len(options[functions]["PARAMETERS"]) <= 0:
            options[functions]["FUNCTION"]()
        
        else:
            options[functions]["FUNCTION"](options[functions]["PARAMETERS"])
    
    