import tkinter as tk
from tkinter import ttk


# Create the root window
root = tk.Tk()
root.title('Hello GUIs')
root.geometry('600x400')

# Create the main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)


# Add label
ttk.Label(frame_home, text="Enter Name: ").grid(column=0, row=0)
ttk.Label(frame_home, text="XYZ").grid(column=1, row=1)

root.mainloop()
