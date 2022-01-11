import tkinter as tk
from tkinter import ttk


def submit_action():
    name = string_user_name.get()
    age = string_user_age.get()
    if int(age) > 18:
        string_message.set(f'{name} please get vaccinated')

# Create the root window
root = tk.Tk()
root.title('hi')
root.geometry('600x200')

# Create the main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)

# Create a label
ttk.Label(frame_home, text="Enter Name: ").grid(column=0, row=0)
ttk.Label(frame_home, text="Enter Age: ").grid(column=0, row=1)

# Create an entry box
string_user_name = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_user_name).grid(column=1, row=0)

# Create an entry box
string_user_age = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_user_age).grid(column=1, row=1)

# Create an entry box
string_message = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_message).grid(column=0, row=3, columnspan=2)

# Create a button
ttk.Button(frame_home, text='submit', command=submit_action).grid(column=0, row=2, columnspan=2)

root.mainloop()
