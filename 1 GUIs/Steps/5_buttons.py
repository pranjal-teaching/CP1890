import tkinter as tk
from tkinter import ttk

def submit_action():
    print(string_user_name.get())

# Create the root window
root = tk.Tk()
root.title('Hello GUIs')
root.geometry('600x400')

# Create the main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)


# Add label
ttk.Label(frame_home, text="Enter Name: ").grid(column=0, row=0)

# Create an entry box
# Entry must have "textvariable"
string_user_name = tk.StringVar() # step 4.1
ttk.Entry(frame_home, width=30, textvariable=string_user_name).grid(column=1, row=0, padx=10, pady=10, ipadx=30, ipady=30) # step 4.2

# step 5
# buttons must have "command"
ttk.Button(frame_home, text='submit', command=submit_action).grid(column=0, row=2, columnspan=2, rowspan=2)


root.mainloop()
