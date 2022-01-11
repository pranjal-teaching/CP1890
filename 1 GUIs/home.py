import tkinter as tk
from tkinter import ttk

# Create the root window
root = tk.Tk()
root.title('hi')
root.geometry('400x200')

# Create the main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)

# Create a label
ttk.Label(frame_home, text="Enter Name: ").grid(column=0, row=0)

# Create an entry box
string_user_name = tk.StringVar()
entry_name = ttk.Entry(frame_home, width=30, textvariable=string_user_name).grid(column=1, row=0)

root.mainloop()
