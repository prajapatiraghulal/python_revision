import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box


win = tk.Tk()
win.title('messages')

name_label = ttk.Label(win, text='Name: ')
name_label.grid(row=0,column=0)

def func():
    i = name_var.get()
    if i==0:
        m_box.showinfo('info','showinfo')
    elif i==1:
        m_box.showerror('error','showerror')
    else:
        m_box.showwarning('warn','showwarning')

   
# func(int(input('enter number:')))   don't do like this 
name_var = tk.IntVar()
name_entry= ttk.Entry(win, textvariable=name_var)
name_entry.grid(row=0,column=1)

#button
button = tk.Button(win, text='submit',command=func)
button.grid(row=2,column=0, columnspan=2)



win.mainloop()