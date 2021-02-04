# This file is for Hafez project functions
from tkinter import *
from tkinter import ttk
from random import randint
# import subprocess
from subprocess import call
from os import getcwd
from images import Images

# Define a path

path = getcwd()

# Define Functions

def First_page_background(master):
    background_for_First_page = Label(master)
    background_for_First_page.pack()
    background_for_First_page.config(image=2,compound = LEFT)

def Omen():
    x= randint(1,10)
    if x==1:
        subprocess.call("1.jpg",shell=True,cwd=path+"\\images\\")
    if x==2:
        subprocess.call("2.jpg",shell=True,cwd=path+"\\images\\")
    if x==3:
        subprocess.call("3.jpg",shell=True,cwd=path+"\\images\\")
    if x==4:
        subprocess.call("4.jpg",shell=True,cwd=path+"\\images\\")
    if x==5:
        subprocess.call("5.jpg",shell=True,cwd=path+"\\images\\")
    if x==6:
        subprocess.call("6.jpg",shell=True,cwd=path+"\\images\\")
    if x==7:
        subprocess.call("7.jpg",shell=True,cwd=path+"\\images\\")
    if x==8:
        subprocess.call("8.jpg",shell=True,cwd=path+"\\images\\")
    if x==9:
        subprocess.call("9.jpg",shell=True,cwd=path+"\\images\\")
    if x==10:
        subprocess.call("10.jpg",shell=True,cwd=path+"\\images\\")

def in_omen_button(master,event):
    master.config(image=Images)
def out_omen_button():
    pass

def Gallery(master):
    Gallery_page = ttk.Frame(master)
    Gallery_page.pack()
def in_gallery_button():
    pass
def out_gallery_button():
    pass

def pdf():
    pass
def in_pdf_button():
    pass
def out_pdf_button():
    pass
