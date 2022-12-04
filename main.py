import tkinter as tk
import tkinter.font as tkFont 
from tkinter.ttk import *
import unitTests as UT


#This dictionary will contain the results of the tests
#It will store each exercice score to be later computed for the final grade
test_scores= {}

#represents which ex is selected to run the unit tests on
selected_ex = {"selected" : None}

#this dictionary is a mapping between an exercice name and the exercice-button and the result label as a tuple:
## ex : selected_ex{"ex1":(Button1,Label1)}
## this dictionary is filled when we are registering an exercice.

labels_buttons = {}


#functions that will be executed when the buttons are clicked.
#In this context the ex buttons are responsible to indicate to the test runner
# which ex will be tested.
#test that will be executed will be marked green
#the rest will be marked red
exercices = []
def select_ex(button_ref, name):
    selected_ex["selected"] = name
    for elt in labels_buttons:
        labels_buttons[elt][0]["bg"] = "red"
    button_ref["bg"] = "green"



## function that will generate the event handlers for the exercices buttons
def buttonFunctionGen(index,name):
    def ex_button_command():
        select_ex(labels_buttons[exercices[index]["name"]][0], name)
    
    return ex_button_command

##Takes the content of the text box and sends it to the testing module
##Gets back the score from the testing module
##Updates the test_scores dictionary
def sendCode():
    source_code = source_code_entry.get("1.0","end-1c")
    ex = selected_ex["selected"]
    res = UT.runTest(ex,source_code)
    labels_buttons[ex][1]["text"] = "Your grade for {} is {}/5".format(ex,res)
    test_scores[ex] =res
    


root = tk.Tk()
#setting title
root.title("undefined")
#setting window size
width=2000
height=1500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)


#This function is responsible to autogenerate the labels and the buttons corresponding to the exercices.
#Since these ones might be different between each TP, we want them to be as modular as possible.

#The exercices dictionary can contain more granularity to make each element more unique.
#For now, the only thing we care about is the text and the corresponding function.
def registerExercices(exercices):
    i=0
    local_y = 0
    for n in exercices:
        ex=tk.Button(root)
        ex["bg"] = "#f0f0f0"
        ft= tkFont.Font(family='Times',size=10)
        ex["font"] = ft
        ex["fg"] = "#000000"
        ex["justify"] = "center"
        ex["text"] = exercices[i]["name"]
        ex.place(x=20,y=60 +local_y,width=120,height=40)
        ex["command"] = exercices[i]["eventHandler"]
        res_ex=Label()
        res_ex["text"] = "{} results = 0/5".format(exercices[i]["name"])
        res_ex.place(x=1700, y=20+local_y)
        labels_buttons[exercices[i]["name"]] = (ex,res_ex)
        i+=1
        local_y+=60
    return 0


##Submit button is responsible for triggering the sendCode function that will communicate with the testing module
submitButton=tk.Button(root)
submitButton["bg"] = "#f0f0f0"
ft= tkFont.Font(family='Times',size=10)
submitButton["font"] = ft
submitButton["fg"] = "#000000"
submitButton["justify"] = "center"
submitButton["text"] = "Submit"
submitButton.place(x=20,y=240,width=120,height=40)
submitButton["command"] = sendCode


#The text box that the student will paste their source code in.
source_code_entry = tk.Text(root)
source_code_entry.place(x=300,y=120,width=1000, height=1000)


#Defining the exercices
#Registering the exercices.
exercices = [{"eventHandler" : buttonFunctionGen(0,"ex1") , "name" : "ex1"},
             {"eventHandler" :  buttonFunctionGen(1,"ex2"), "name" : "ex2"},
             {"eventHandler" : buttonFunctionGen(2,"ex3"), "name" : "ex3"},
             {"eventHandler" : buttonFunctionGen(3,"ex4"), "name" : "ex4"}]

registerExercices(exercices)
root.mainloop()