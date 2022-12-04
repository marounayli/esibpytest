import tkinter as tk
import tkinter.font as tkFont 
from tkinter.ttk import *
import unitTests as UT


#represents which ex is selected to run the unit tests on
selected_ex = {"selected" : None}

labels_buttons = {}


#functions that will be executed when the buttons are clicked.
#In this context the ex buttons are responsible to indicate to the test runner
# which ex will be tested.
#test that will be executed will be marked green
#the rest will be marked red

def select_ex(button_ref, name):
    selected_ex["selected"] = name
    global buttons
    for b in buttons:
        b["bg"] = "red"
    button_ref["bg"] = "green"

def ex1Button_command():
    select_ex(ex1,"ex1")

def ex2Button_command():
    select_ex(ex2,"ex2")

def ex3Button_command():
    select_ex(ex3,"ex3")


def sendCode():
    source_code = source_code_entry.get("1.0","end-1c")
    res = UT.runTest(selected_ex["selected"],source_code)
    labels_buttons[selected_ex["selected"]][1]["text"] = "Your grade for {} is {}/5".format(selected_ex["selected"],res)
    



buttons = []
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
ex1=tk.Button(root)
ex1["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
ex1["font"] = ft
ex1["fg"] = "#000000"
ex1["justify"] = "center"
ex1["text"] = "ex1"
ex1.place(x=20,y=60,width=120,height=40)
ex1["command"] = ex1Button_command
buttons.append(ex1)
ex2=tk.Button(root)
ex2["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
ex2["font"] = ft
ex2["fg"] = "#000000"
ex2["justify"] = "center"
ex2["text"] = "ex2"
ex2.place(x=20,y=120,width=120,height=40)
ex2["command"] = ex2Button_command
buttons.append(ex2)
ex3=tk.Button(root)
ex3["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
ex3["font"] = ft
ex3["fg"] = "#000000"
ex3["justify"] = "center"
ex3["text"] = "ex3"
ex3.place(x=20,y=180,width=120,height=40)   
ex3["command"] = ex3Button_command

ex4=tk.Button(root)
ex4["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
ex4["font"] = ft
ex4["fg"] = "#000000"
ex4["justify"] = "center"
ex4["text"] = "Submit"
ex4.place(x=20,y=240,width=120,height=40)
ex4["command"] = sendCode

res_ex1 =Label()
res_ex1["text"] = "Ex1 results = 0/5"
res_ex1.place(x=1700, y=20)

res_ex2 =Label()
res_ex2["text"] = "Ex2 results = 0/5"
res_ex2.place(x=1700, y=120)

res_ex3=Label()
res_ex3["text"] = "Ex3 results = 0/5"
res_ex3.place(x=1700, y=220)



labels_buttons["ex1"] = (ex1,res_ex1)
labels_buttons["ex2"] = (ex2,res_ex2)
labels_buttons["ex3"] = (ex3,res_ex3)
buttons.append(ex3)

source_code_entry = tk.Text(root)
source_code_entry.place(x=300,y=120,width=1000, height=1000)
root.mainloop()