
import os
import pandas as pd
from openpyxl import load_workbook
from tkinter import *

root = Tk()

def newclick1():
     newbutton = Button(root, text="CALCULATOR START-UP TEST CASE", command=file, fg="blue")
     newbutton.pack()

def myClick():
    mybutton1 = Button(root, text="Click for Basic Operational Tests",  command=newclick1, fg="orange")
    mybutton1.pack()
    mybutton2 = Button(root, text="Click for Functionality Test Cases", fg="blue")
    mybutton2.pack()
    mybutton3 = Button(root, text="Click for Advanced Tests on Scientific Calculator", fg="green")
    mybutton3.pack()

def file() :
    try:
        os.startfile("C:\\Users\\adaka\\Desktop\\newpythonpro\\test_case_1.xlsx")
    except FileNotFoundError:
        print("file does not exist :(")




myLabel = Label(root, text="welcome to chat bot", fg="red")
myLabel.pack()

mybutton = Button(root, text="click for test suites", command=myClick, fg="orange")

mybutton.pack()

root.mainloop()