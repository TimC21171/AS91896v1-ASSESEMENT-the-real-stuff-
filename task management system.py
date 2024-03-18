

import easygui

tasks = {
    
    "T1": {
        
        "TITLE": "Design Homepage",
        "DESCRIPTION": "Create a mockup of the homepage",
        "ASSIGNEE": "JSM",
        "PRIORITY": "3",
        "STATUS": "In progress",
        
    },
    
    "T2": {
        
        "TITLE": "Implement Login page",
        "DESCRIPTION": "Create the Login page for the website",
        "ASSIGNEE": "JSM",
        "PRIORITY": "3",
        "STATUS": "Blocked",
        
    },
    
    "T3": {
        
        "TITLE": "Fix navigation",
        "DESCRIPTION": "Fix tha navigation menu to be more user-friendly",
        "ASSIGNEE": "None",
        "PRIORITY": "1",
        "STATUS": "Not started",
        
    },
    
    "T4": {
        
        "TITLE": "Add payment processing",
        "DESCRIPTION": "Implement payment processing for the website",
        "ASSIGNEE": "JLO",
        "PRIORITY": "",
        "STATUS": "In progress",
        
    },
    
    "T5": {
        
        "TITLE": "Create an About Us page",
        "DESCRIPTION": "Create a page with information about the company",
        "ASSIGNEE": "BDI",
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

options = {
    
    "See project progress report":{
        
        "FUNCTION": show_all,
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
    
    