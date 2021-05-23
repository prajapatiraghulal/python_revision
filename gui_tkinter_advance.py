import tkinter
import tkinter as tk
from tkinter import  ttk

win = tkinter.Tk()
win.title('loop')
label_frame = ttk.Labelframe(win, text='  trial')               #Label frame creation in main win
label_frame.grid(row=0,column=0)

list_labels = ['NAME:','EMAIL:','AGE:','GENDER']
# labels_name = [ttk.Label(win,text=s).grid(row=i,column=0,sticky=tk.W) for i,s in enumerate(list_labels)]
ll =[]
for i,s in enumerate(list_labels):
    temp= ttk.Label(label_frame,text=s)
    temp.grid(row=i,column=0,sticky=tk.W, padx=20,pady=20)
    ll.append(temp)
# for l in list_labels:
name_label = ttk.Label(win,text='Name: ')
name_label.grid(row=1,column=0)

for child in label_frame.winfo_children():
    child.grid_configure(padx=5,pady=5)     #changed padding previously defined for all child in frame

print(name_label)

print(type(ll[0]), temp)


win.mainloop()