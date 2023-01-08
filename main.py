import tkinter as tk
import tkinter.font as tkFont 
from tkinter.ttk import *
import unitTests as UT
import encModule


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


def generateGradeFile():
    encModule.encrypt_grades(test_scores)

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
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
width=screenwidth/2
height=screenwidth/2
# alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry('1000x600')
root.resizable(width=False, height=False)
root.configure(background = "#FAFBFC")
frame = tk.Frame(root, background="#FAFBFC")
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)

#This function is responsible to autogenerate the labels and the buttons corresponding to the exercices.
#Since these ones might be different between each TP, we want them to be as modular as possible.

#The exercices dictionary can contain more granularity to make each element more unique.
#For now, the only thing we care about is the text and the corresponding function.
def registerExercices(exercices, frame: tk.Frame):
    i=0
    local_y = 0
    
    mainFrame = tk.Frame(frame, bg="#FAFBFC")
    
    titleFt = tkFont.Font(family='Inter',size=32, weight='bold')
    
    title = tk.Label(mainFrame, text="Exercises")
    title["font"] = titleFt
    title["fg"] = "#333333"
    title["bg"] = "#FAFBFC"
    title.grid(column=0, row=0, pady=20, padx=10)
    # title.pack()
    
    descFt = tkFont.Font(family='Inter',size=12)
    desc = tk.Label(mainFrame, text="Please select one of the exercises for submission:")
    desc["font"] = descFt
    desc["fg"] = "#666666"
    desc["bg"] = "#FAFBFC"
    desc.grid(column=0, row=1, padx= 10, pady=20)
    # desc.pack()
    
    # Exercises frame that contains all the exercises buttons
    exFrame = tk.Frame(mainFrame, background="#FAFBFC")
    exFrame.columnconfigure(0,weight=1)
    exFrame.grid(column=0, row=2)
    for n in exercices:
        ex=tk.Button(exFrame,borderwidth=0)
        ex["bg"] = "#0284C7"
        ft = tkFont.Font(family='Inter',size=12)
        ex["font"] = ft
        ex["fg"] = "#ffffff"
        ex["justify"] = "center"
        ex["text"] = exercices[i]["name"]
        # ex.place(x=20,y=60 +local_y,width=120,height=40)
        ex.grid(column=0, row=i, padx= 10, pady=10, ipadx=48, ipady=8)
        ex["command"] = exercices[i]["eventHandler"]
        res_ex=Label()
        res_ex["text"] = "{} results = 0/5".format(exercices[i]["name"])
        res_ex.place(x=1300, y=20+local_y)
        labels_buttons[exercices[i]["name"]] = (ex,res_ex)
        i+=1
        local_y+=60
    # mainFrame.place(x=20, y=20)
    mainFrame.grid(column=0, row=0, ipadx=10, ipady=10)
    return 0


##Submit button is responsible for triggering the sendCode function that will communicate with the testing module
submitButton=tk.Button(frame, borderwidth=0)
submitButton["bg"] = "#0284C7"
ft= tkFont.Font(family='Inter',size=12)
submitButton["font"] = ft
submitButton["fg"] = "#ffffff"
submitButton["justify"] = "center"
submitButton["text"] = "Submit"
# submitButton.place(x=20,y=1000,width=120,height=40)
submitButton.grid(column=0, row=1, padx= 10, pady=10, ipadx=48, ipady=8, columnspan=2)
submitButton["command"] = sendCode


finalSubmitButton=tk.Button(frame, borderwidth=0)
finalSubmitButton["bg"] = "#0284C7"
ft= tkFont.Font(family='Inter',size=12)
finalSubmitButton["font"] = ft
finalSubmitButton["fg"] = "#ffffff"
finalSubmitButton["justify"] = "center"
finalSubmitButton["text"] = "Generate Grades File"
# finalSubmitButton.place(x=20,y=1200,width=300,height=40)
finalSubmitButton.grid(column=0, row=2, padx= 10, pady=10, ipadx=48, ipady=8, columnspan=2)
finalSubmitButton["command"] = generateGradeFile


# testb = tk.Button(root)
# img = tk.PhotoImage(file="images/ex1-icon.png")
# testb.config(image=img)
# finalSubmitButton.place(x=20,y=1300,width=300,height=40)



#The text box that the student will paste their source code in.
source_code_entry = tk.Text(frame)
source_code_entry.grid(column=1, row=0)
# source_code_entry.place(x=300,y=120,width=1000, height=1000)


#Defining the exercices
#Registering the exercices.
exercices = [{"eventHandler" : buttonFunctionGen(0,"ex1") , "name" : "ex1"},
             {"eventHandler" :  buttonFunctionGen(1,"ex2"), "name" : "ex2"},
             {"eventHandler" : buttonFunctionGen(2,"ex3"), "name" : "ex3"},
             {"eventHandler" : buttonFunctionGen(3,"ex4"), "name" : "ex4"}]

registerExercices(exercices, frame)
frame.pack(ipadx=10, ipady=10)
root.mainloop()