import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Example GUI 2 Program")
win.geometry("200x100")

frame = tk.Frame(win, background="red")
frame.pack(fill=tk.BOTH, expand=True)

def click_button1():
    win.title("You clicked the button!")

button1 = tk.Button(frame,text="Click me!", command=click_button1, background="blue")
button1.pack()

win.mainloop()