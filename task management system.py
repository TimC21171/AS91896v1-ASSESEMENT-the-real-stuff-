#new change: 26/3/24



import easygui, sys

#tasks dictionary
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

#team members dictionary
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


#questions function
def question(data):
    
    
    """ 
    Quesion function recieves input from the data parameter,
    and based on the input into the function it executes
    specific tasks.
    """
    
    response = None
    
    #while loop that prevents invalid responses such as None
    while response == None:

        #executes different tasks based on the "input type" key from the data parameter
        
        if data["input type"] == "typing":
            response = easygui.enterbox(data["given string"])
            
        elif data["input type"] == "buttons":
            response = easygui.buttonbox(data["given string"], choices=data["options"])
            
        elif data["input type"] == "int":
            response = easygui.integerbox(data["given string"])
        
        #returns response var if user input is valid
        if response != None:
            return response
        
        #otherwise while loop continues
        else:
            leave = None
            
            #while loop that prevents invalid responses such as None
            while response == None:
                leave = easygui.buttonbox("Are you sure you want to leave?", choices = ["Yes", "No"])
                
                if leave != None:
                    if leave == "Yes":
                        sys.exit()
                    else:
                        break
                
                else:
                    easygui.msgbox("Please enter an input")

def show_all(data):
    
    """
    show_all function displays text from dictionaries
    or values inside of a key based on the input into 
    the function
    """
    
    final_str = f""
    
    #executes different for loops depending on the desired settings
    
    #executes if input wants a whole dictionary to be displayed
    if data["data type"] == "dict":
        for id in data["parent"]:
            final_str += f"\n\n{id}: \n\n"
            for values in data["parent"][id]:
                final_str += f"{values}: {data['parent'][id][values]}\n"
                
    #executes if input wants to only display values in a key
    elif data["data type"] == "keys":
        final_str += f"{[data['key']]}\n\n"
        for val in data["parent"][data["key"]]:
            final_str += f"{val}: {data['parent'][data['key']][val]}\n"
            

    easygui.msgbox(final_str)
    

def add_task():
    
    
    """
    Automates making a new task ID
    as well as asks the user input
    to set for the values in the task
    ID key
    """
    
    #gives a new task ID based on the amount of tasks there are
    task_number = len(tasks) + 1
    final_task_number = f"T{task_number}"
    
    #sets the formed task ID as an actual key part of the tasks dict
    tasks[final_task_number] = {}
    
    #calls function that edits the newly made task ID key
    edit_key_val({"input_data_key": final_task_number, "data type": "task", "parent": None, "task type": "new"})
    
    show_all({"parent": tasks, "data type": "keys", "key": final_task_number})
    
def update_task():
    
    chosen_task = search({
    "question": "Choose a task to update",
    "options": list(tasks),
    "dict": tasks,
    "forceSearchType": "buttons",
    "shouldReturn": True,
    })
    
    edit_key_val({"input_data_key": chosen_task, "data type": "task", "parent": None, "task type": "existing"})
    
    for members in team_members:
        for i in range(len(team_members[members]["Tasks assigned"])):
            if chosen_task in team_members[members]["Tasks assigned"][i]:
                if members in tasks[chosen_task]["ASSIGNEE"] == False:
                    team_members[members]["Tasks assigned"].remove(chosen_task)

    show_all({"parent": tasks, "data type": "keys", "key": chosen_task})
    
def check_completed(given_task):
    if tasks[given_task]["STATUS"] == "Completed" or tasks[given_task]["ASSIGNEE"] == "None":
        for members in team_members:
            exists = given_task in team_members[members]["Tasks assigned"]
            if exists:
                team_members[members]["Tasks assigned"].remove(given_task)
        
def progress_report():
    
    data = {
      
      
        "PROGRESS_DATA":{
            
            "In progress": {"number of tasks": 0},
            "Not started": {"number of tasks": 0},
            "Blocked": {"number of tasks": 0},
            "Completed": {"number of tasks": 0},  
            
        }
        
    }
    
    for task_id in tasks:
        data["PROGRESS_DATA"][tasks[task_id]["STATUS"]]["number of tasks"] += 1
        
    show_all({"parent": data, "data type": "dict"})
        
        
def edit_key_val(data):
    
    """
    function that makes/edits values in a given key
    from the data parameter
    """
    
    #executes if input is specifically for editing a task
    if data["data type"] == "task":
        
        #temporary members dict var
        temp_members_dict = {}
        
        for possible_member in team_members:

            #adds a team member to the temporary dict
            #this will be used to help display the buttons nicely
            temp_members_dict[possible_member] = {}
            temp_members_dict[possible_member]["NAME"] = team_members[possible_member]['Name']
            
        #adds the option of None
        temp_members_dict["None"] = {}
        temp_members_dict["(Stop adding members)"] = {}
        original_temp_members_len = len(temp_members_dict)

        #2D list that contains specific questions and values for editing the task values
        new_task_values = [["Give a title for this new task: ", "TITLE", None], 
                        ["Give a description for this new task: ", "DESCRIPTION", None],
                        ["Add people to work on this task", "ASSIGNEE"],
                        ["From 1-3, how important is this task?", "PRIORITY"],
                        ["Choose a status for this task", "STATUS", 
                            ["In progress", "Not started", "Blocked", "Completed"]]]
            
        #loops through the new_task_values list
        for i in range(len(new_task_values)):
            
            
            """ 
            for loop executes specific code based on
            the i[1] value from new_task_values list
            """
            
            #executes if the looped variable i[1] is currently at "ASSIGNEE"
            if new_task_values[i][1] == "ASSIGNEE":
                
                #empty variable
                chosen_member = ""
                
                #flag
                looped_once = False
                
                #resets the tasks: "ASIGNEE" value as an empty list
                tasks[data["input_data_key"]][new_task_values[i][1]] = []
                
                #infinite loop
                while True:
                    
                    """ 
                    Loop continues going through
                    until user decides to stop adding members
                    or until all members from the
                    team_members dictionary have been chosen
                    """
                        
                    """ 
                    Calls the search function and searches the
                    temporary_member_dict, search function data
                    inputs to ask the user: 'Choose a member to pick from',
                    to only make the user to navigate their searching
                    experience using buttons with the set 'forceSearchType' value
                    and tells the search function to return the chosen option
                    """
                    
                    #chosen_member variable hold returned value from search function
                    chosen_member = search({
                    "question": "Choose a member to pick from",
                    "options": list(temp_members_dict),
                    "dict": temp_members_dict,
                    "forceSearchType": "buttons",
                    "shouldReturn": True,
                    })
                    
                    if chosen_member == "None" or chosen_member == "(Stop adding members)":
                        if chosen_member == "None" or chosen_member == "(Stop adding members)" and len(temp_members_dict) == original_temp_members_len:
                            tasks[data["input_data_key"]][new_task_values[i][1]] = "None"
                        break
                    
                    else:

                        tasks[data["input_data_key"]][new_task_values[i][1]].append(chosen_member)
                        exists = data["input_data_key"] in team_members[chosen_member]["Tasks assigned"]
                        if exists == False:    
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
                
                if given_status == "Completed":
                    tasks[data["input_data_key"]]["ASSIGNEE"] = "None"
                    for members in team_members:
                        exists = data["input_data_key"] in team_members[members]["Tasks assigned"]
                        if exists:
                            team_members[members]["Tasks assigned"].remove(data["input_data_key"])
                
                tasks[data["input_data_key"]][new_task_values[i][1]] = given_status
                
            elif data["task type"] == "new":
                                
                entered_task_val =  question({
                    "input type": "typing",
                    "options": None,
                    "given string": new_task_values[i][0]
                })
                
                tasks[data["input_data_key"]][new_task_values[i][1]] = entered_task_val
                
        check_completed(data["input_data_key"])
    
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
    
    "See all tasks":{
        
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
        
    },
    
    "Update a task":{
        
        "FUNCTION": update_task,
        "PARAMETERS": {},
        
    },
    
    "Show progress report":{
        
        "FUNCTION": progress_report,
        "PARAMETERS": {}
        
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
    
    