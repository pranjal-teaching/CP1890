import tkinter as tk
from tkinter import ttk

def click_button1():
    root.title("You clicked button 1")

def click_button2():
    root2 = tk.Tk()
    root2.title("Future Value Calculater")
    root2.geometry("500x400")
    root2.mainloop()

def close():
    root.destroy()

root = tk.Tk()
root.title("Future Value Calculater")
root.geometry("500x300")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

button1 = ttk.Button(frame, text="Click me!", command=click_button1)
button2 = ttk.Button(frame, text="No Click me!", command=click_button2)
button3 = ttk.Button(frame, text="Close", command=close)

investmentLabel = ttk.Label(frame, text="Monthly Investment").grid(column=0, row=0)


investmentText = tk.StringVar()
investmentEntry = ttk.Entry(frame, width=25, textvariable=investmentText).grid(column=1, row=0)

for child in frame.winfo_children():
    child.grid_configure(padx=10,pady=10)


root.mainloop()