import tkinter as tk
import tkinter.font as tkFont 
from tkinter.ttk import *


#represents which ex is selected to run the unit tests on
selected_ex = {"selected" : None}


#functions that will be executed when the buttons are clicked.
#In this context the ex buttons are responsible to indicate to the test runner
# which ex will be tested.




def ex1Button_command():
    selected_ex["selected"] = "ex1"

def ex2Button_command():
    selected_ex["selected"] = "ex2"

def ex3Button_command():
    selected_ex["selected"] = "ex3"



buttons = []
root = tk.Tk()
#setting title
root.title("undefined")
#setting window size
width=1200
height=800
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
ex1["text"] = "Button"
ex1.place(x=20,y=60,width=120,height=40)
ex1["command"] = ex1Button_command
buttons.append(ex1)
ex2=tk.Button(root)
ex2["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
ex2["font"] = ft
ex2["fg"] = "#000000"
ex2["justify"] = "center"
ex2["text"] = "Button"
ex2.place(x=20,y=120,width=120,height=40)
ex2["command"] = ex2Button_command
buttons.append(ex2)
ex3=tk.Button(root)
ex3["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
ex3["font"] = ft
ex3["fg"] = "#000000"
ex3["justify"] = "center"
ex3["text"] = "Button"
ex3.place(x=20,y=180,width=120,height=40)
ex3["command"] = ex3Button_command
buttons.append(ex3)
source_code = tk.Text(root)
source_code.place(x=300,y=100,width=500, height=500)
root.mainloop()