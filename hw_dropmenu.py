import tkinter as tk
from tkinter import Menu

# Function definitions for menu actions
def new_file():
    print("New File Created")

def open_file():
    print("File Opened")

def save_file():
    print("File Saved")

def cut():
    print("Cut")

def copy():
    print("Copy")

def paste():
    print("Paste")

def zoom_in():
    print("Zoomed In")

def zoom_out():
    print("Zoomed Out")

def tools_options():
    print("Tools Options Opened")

def show_help():
    print("Help Dialog Opened")

# Creating the main window
root = tk.Tk()
root.title("Menubar Example")

# Creating the menubar
menubar = Menu(root)

# File menu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
menubar.add_cascade(label="Edit", menu=edit_menu)

# View menu
view_menu = Menu(menubar, tearoff=0)
view_menu.add_command(label="Zoom In", command=zoom_in)
view_menu.add_command(label="Zoom Out", command=zoom_out)
menubar.add_cascade(label="View", menu=view_menu)

# Tools menu
tools_menu = Menu(menubar, tearoff=0)
tools_menu.add_command(label="Options", command=tools_options)
menubar.add_cascade(label="Tools", menu=tools_menu)

# Help menu
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="Help", command=show_help)
menubar.add_cascade(label="Help", menu=help_menu)

# Configuring the menubar
root.config(menu=menubar)

# Running the application
root.mainloop()

