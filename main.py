# This is a main file for the Hafez project

#importing modules
from tkinter import *
from tkinter import ttk
import subprocess
import random
import time
import os
import images
import functions

# Define a path

path = os.getcwd()

# create window & Changes

root = Tk()

root.title("حافظ")

root.geometry("800x600+10+10")

root.resizable(False,False)

# root.iconbitmap(path+"\\icon.ico")

# Define Buttons and Labels and Panedwindow and Pages

PanedWindow_of_root = ttk.PanedWindow(root,orient=HORIZONTAL)
PanedWindow_of_root.pack(fill=BOTH,expand=True)

First_page = ttk.Frame(PanedWindow_of_root, height=600, width=800)
First_page.pack()

Omen_button = Button(First_page,
                        image=images.Images,
                        bd = 0,
                        height=100,
                        width=200,
                        command=None    )
Omen_button.place(x=0,y=0)


# mainloop

root.mainloop()
