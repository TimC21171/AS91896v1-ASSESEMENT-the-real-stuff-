import easygui


response = None

while response == None:
    response = easygui.enterbox("u black?")
    
    if response != None:
        break
    else:
        easygui.msgbox("What the flip dawg dont leave") 
        
        