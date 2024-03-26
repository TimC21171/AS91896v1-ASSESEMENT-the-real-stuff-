import easygui

dictionary = {
    "T1":{
        
        "Title": "Some task",
        "eh": "asdasdasd",
        
    },
    "T2": {
        
        "Title": "Some other task from task 2",
        "eh": "boo"
        
    }
}

buttons = []

for values in dictionary:
    buttons.append(dictionary[values]["Title"])
    
response = easygui.buttonbox("Pick something", choices= buttons)
    