import tkinter as tk
from tkinter import ttk


# Create the root window
root = tk.Tk()
root.title('hi')
root.geometry('400x200')
root.mainloop()

frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)
