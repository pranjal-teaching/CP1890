import tkinter as tk
from tkinter import ttk

class InvestmentFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self,parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)

        self.monthlyInvestment = tk.StringVar()

        ttk.Label(self, text="Monthly Investment:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.monthlyInvestment).grid(column=1,row=0)
        ttk.Button(self, text="Clear", command=self.clear).grid(column=2, row=0)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def clear(self):
        print("Monthly Investment:", self.monthlyInvestment.get())
        self.monthlyInvestment.set("")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Future Value Calculator")
    InvestmentFrame(root)
    root.mainloop()