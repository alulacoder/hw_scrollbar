import tkinter as tk
from tkinter import ttk

def create_listbox_with_scrollbar():
    # Create the main window
    root = tk.Tk()
    root.title("Listbox with Scrollbar")

    # Create a frame to contain the Listbox and Scrollbar
    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Create the Listbox
    listbox = tk.Listbox(frame, height=10, width=30)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    # Add items to the Listbox
    items = [f"Item {i}" for i in range(1, 101)]  # Example items from 1 to 100
    for item in items:
        listbox.insert(tk.END, item)

    # Create the Scrollbar
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the Listbox to work with the Scrollbar
    listbox.config(yscrollcommand=scrollbar.set)

    # Run the Tkinter event loop
    root.mainloop()

# Call the function to run the application
create_listbox_with_scrollbar()
