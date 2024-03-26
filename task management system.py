#new change: 26/3/24

import easygui

tasks = {
    
    "T1": {
        
        "TITLE": "Design Homepage",
        "DESCRIPTION": "Create a mockup of the homepage",
        "ASSIGNEE": ["JSM"],
        "PRIORITY": 3,
        "STATUS": "In progress",
        
    },
    
    "T2": {
        
        "TITLE": "Implement Login page",
        "DESCRIPTION": "Create the Login page for the website",
        "ASSIGNEE": ["JSM"],
        "PRIORITY": 3,
        "STATUS": "Blocked",
        
    },
    
    "T3": {
        
        "TITLE": "Fix navigation",
        "DESCRIPTION": "Fix tha navigation menu to be more user-friendly",
        "ASSIGNEE": "None",
        "PRIORITY": 1,
        "STATUS": "Not started",
        
    },
    
    "T4": {
        
        "TITLE": "Add payment processing",
        "DESCRIPTION": "Implement payment processing for the website",
        "ASSIGNEE": ["JLO"],
        "PRIORITY": 2,
        "STATUS": "In progress",
        
    },
    
    "T5": {
        
        "TITLE": "Create an About Us page",
        "DESCRIPTION": "Create a page with information about the company",
        "ASSIGNEE": ["BDI"],
        "PRIORITY": 1,
        "STATUS": "Blocked",
        
    },
    
}

team_members = {
    
    "JSM": {
        
        "Name": "John Smith",
        "Email": "John@techvision.com",
        "Tasks assigned": ["T1", "T2"]
        
    },
    
    "JLO": {
        
        "Name": "Jane Love",
        "Email": "Jane@techvision.com",
        "Tasks assigned": ["T4"]
        
    },
    
    "BDI": {
        
        "Name": "Bob Dillon",
        "Email": "Bob@techvision.com",
        "Tasks assigned": ["T5"]
        
    },
    
}


def question(data):
    
    response = None
    
    while response == None:

        if data["input type"] == "typing":
            response = easygui.enterbox(data["given string"])
            
        elif data["input type"] == "buttons":
            response = easygui.buttonbox(data["given string"], choices=data["options"])
            
        elif data["input type"] == "int":
            response = easygui.integerbox(data["given string"])
        
        if response != None:
            return response
        else:
            easygui.msgbox("Please enter an input")

def show_all(data):
    
    final_str = f""
    
    if data["data type"] == "dict":
        for id in data["parent"]:
            final_str += f"\n\n{id}: \n\n"
            for values in data["parent"][id]:
                final_str += f"{values}: {data['parent'][id][values]}\n"
                
    elif data["data type"] == "keys":
        final_str += f"{[data['key']]}\n\n"
        for val in data["parent"][data["key"]]:
            final_str += f"{val}: {data['parent'][data['key']][val]}\n"
            
            
    easygui.msgbox(final_str)
    
def add_task():
    
    task_number = len(tasks) + 1
    final_task_number = f"T{task_number}"
    tasks[final_task_number] = {}
    
    edit_key_val({"input_data_key": final_task_number, "data type": "task", "parent": None})
    
    show_all({"parent": tasks, "data type": "keys", "key": final_task_number})
        
def edit_key_val(data):
    
    if data["data type"] == "task":
        
        temp_members_dict = {}
        
        for possible_member in team_members:
            temp_members_dict[possible_member] = {}
            temp_members_dict[possible_member]["NAME"] = team_members[possible_member]['Name']
            
        temp_members_dict["None"] = {}
        temp_members_dict["(Stop adding members)"] = {}

        new_task_values = [["Give a title for this new task: ", "TITLE", None], 
                        ["Give a description for this new task: ", "DESCRIPTION", None],
                        ["Add people to work on this task", "ASSIGNEE"],
                        ["From 1-3, how important is this task?", "PRIORITY"],
                        ["Choose a status for this task", "STATUS", 
                            ["In progress", "Not started", "Blocked"]]]
            
        for i in range(len(new_task_values)):
            if new_task_values[i][1] == "ASSIGNEE":
                chosen_member = ""
                looped_once = False
                
                tasks[data["input_data_key"]][new_task_values[i][1]] = []
                
                while True:
                        
                    chosen_member = search({
                    "question": "Choose a member to pick from",
                    "options": list(temp_members_dict),
                    "dict": temp_members_dict,
                    "forceSearchType": "buttons",
                    "shouldReturn": True,
                    })
                    
                    if chosen_member == "None" or chosen_member == "(Stop adding members)":
                        if chosen_member == "None":
                            tasks[data["input_data_key"]][new_task_values[i][1]] = chosen_member
                        break
                    
                    else:

                        tasks[data["input_data_key"]][new_task_values[i][1]].append(chosen_member)
                        team_members[chosen_member]["Tasks assigned"].append(data["input_data_key"])
                        del temp_members_dict[chosen_member]
                        
                        if len(temp_members_dict) <= 1:
                            break
                        
                        if looped_once == False:
                            del temp_members_dict["None"]
                            looped_once = True
                    
            elif new_task_values[i][1] == "PRIORITY":
                while True:
                    priority =  question({
                        "input type": "int",
                        "options": None,
                        "given string": new_task_values[i][0]
                    })

                    if priority > 0 and priority <= 3:
                        tasks[data["input_data_key"]][new_task_values[i][1]] = priority
                        break
                    else:
                        easygui.msgbox("Out of range. Enter values between 1-3")
                
            elif new_task_values[i][1] == "STATUS":
                
                given_status =  question({
                    "input type": "buttons",
                    "options": new_task_values[i][2],
                    "given string": new_task_values[i][0]
                })
                
                tasks[data["input_data_key"]][new_task_values[i][1]] = given_status
                
            else:
                                
                entered_task_val =  question({
                    "input type": "typing",
                    "options": None,
                    "given string": new_task_values[i][0]
                })
                
                tasks[data["input_data_key"]][new_task_values[i][1]] = entered_task_val
    
    elif data["data type"] == "other" and data["parent"] != None:
        
        chosen_id = search({
            "question": "Choose from the given to edit:",
            "options": list(data["parent"]),
            "dict": data["parent"],
            "forceSearchType": "buttons",
            "shouldReturn": True,
        })
        
        for val_key in data["parent"][chosen_id]:
        
            new_value =  question({
                "input type": "typing",
                "options": None,
                "given string": f"Enter a new value for {val_key}:"
            })
            
            data["parent"][val_key] = new_value
            
        show_all({"parent": data["parent"], "data type": "keys", "key": chosen_id})
            
def update_task():
    chosen_task = search({
            "question": "Choose a member to pick from",
            "options": list(tasks),
            "dict": tasks,
            "forceSearchType": "None",
            "shouldReturn": True,
        })
    
    for value in tasks[chosen_task]:
        new_value = easygui.enterbox("")

        
def search(data):
    
    search_types_list = ["Button search", "Search through typing"]
    search_type = ""

    if data["forceSearchType"] == "None":
        search_type =  question({
            "input type": "buttons",
            "options": search_types_list,
            "given string": "Pick a search type: "
        })
    
    #button search
    if search_type == search_types_list[0] or data["forceSearchType"] == "buttons":
        
        chosen_val =  question({
            "input type": "buttons",
            "options": data["options"],
            "given string": data["question"]
        })
        
        if data["shouldReturn"]:
            return chosen_val
        else:
            show_all({"parent": data["dict"], "data type": "keys", "key": chosen_val})
         
    #typing search
    elif search_type == search_types_list[1] or data["forceSearchType"] == "typing":
        
        while True:
            chosen_val =  question({
                "input type": "typing",
                "options": None,
                "given string": data["question"]
            })
            
            if chosen_val.isnumeric() == False:
                exists = False
                
                for key in data["dict"]:
                    if key.lower() == chosen_val.lower():
                        exists = True
                        
                if exists:
                    if data["shouldReturn"]:
                        return chosen_val.upper()
                    else:
                        show_all({"parent": data["dict"], "data type": "keys", "key": chosen_val.upper()})
                        break
                        
                else:
                    easygui.msgbox("Entered value does not exist in dictionary. Try again.")
            
            else:
                easygui.msgbox("Integers aren't accepted as a valid response. Try again")
            
        
        

options = {
    
    "See project progress report":{
        
        "FUNCTION": show_all,
        "PARAMETERS": {
            
            "parent": tasks,
            "data type": "dict",
            
            },
        
    },
    
    "Search for Members":{
      
        "FUNCTION": search,
        "PARAMETERS": {
            "question": "What member are you searching for?",
            "options": list(team_members),
            "dict": team_members,
            "forceSearchType": "None",
            "shouldReturn": False,
        },  
        
    },
    
    "Search for Tasks":{
      
        "FUNCTION": search,
        "PARAMETERS": {
            "question": "What task are you searching for?",
            "options": list(tasks),
            "dict": tasks,
            "forceSearchType": "None",
            "shouldReturn": False,
        },  
        
    },
    
    "Add new task":{
        
        "FUNCTION": add_task,
        "PARAMETERS": {},
        
    }
    
}


given_options = []
for options_functions in options:
    given_options.append(options_functions)
given_options.append("(Leave)")

users_choice = ""
while True:
    users_choice =  question({
        "input type": "buttons",
        "options": given_options,
        "given string": "What would you like to do?"
    })
    if users_choice != "(Leave)":
        for functions in options:
            if functions == users_choice:
                if len(options[functions]["PARAMETERS"]) <= 0:
                    options[functions]["FUNCTION"]()
                
                else:
                    options[functions]["FUNCTION"](options[functions]["PARAMETERS"])
                    
    else:
        break
    
    