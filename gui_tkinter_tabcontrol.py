import tkinter
from tkinter import ttk
import tkinter as tk
from typing import Text

win = tkinter.Tk()
win.title("tabbing control")

nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)

nb.add(page1, text='page1')
nb.add(page2, text='page2')

# # # nb.grid(row=0, column=0)      #this creates problem as it does not expand so we use pack 
nb.pack(expand=True, fill='both')

label_page1 = ttk.Label(page1, text='enter name')
label_page1.grid(row=0,column=0)






win.mainloop()