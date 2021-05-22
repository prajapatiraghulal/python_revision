import tkinter as tk 
import tkinter
from tkinter import  ttk

win = tkinter.Tk()
win.title('GUI')
# # # print(dir(tkinter))
# # # print(help(win.title))

#create label
name_label = ttk.Label(win,text='enter name:')
name_label.grid(row=0,column=0,sticky=tk.W)   #tk.W is for west sticking the label

email_label = ttk.Label(win,text='email address: ')
email_label.grid(row=1,column=0,sticky=tk.W)

age_label = ttk.Label(win, text='enter age')
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label = ttk.Label(win,text='select gender: ')
gender_label.grid(row=3,column=0)
# print(help(ttk.Label))

#create entry_box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=20,textvariable=name_var)
name_entrybox.focus()
name_entrybox.grid(row=0,column=1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win,width=20,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=20,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

#create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win,width=20,textvariable=gender_var, state='readonly')
gender_combobox['values']=('male','female','other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

#create radio button
radio_var = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='true',value='true', variable=radio_var)
radiobtn1.grid(row=4,column=0)
radiobtn2 = ttk.Radiobutton(win, text='false',value='false',variable=radio_var)
radiobtn2.grid(row=4,column=1)

#create button
def show():
    with open('entry.txt','a') as f:
        if 4==0:
            f.write(f"'user_name','user_email','user_age','user_gender','user_radio_option'\n")
        f.write(f'{name_var.get()},{email_var.get()},{age_var.get()},{gender_var.get()},{radio_var.get()}\n')
    print(name_var.get(),email_var.get(),age_var.get())
    print(gender_var.get(),radio_var.get())
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    gender_combobox.delete(0,tk.END)
    

button = ttk.Button(win,text='submit',command=show)
button.grid(row=6)



win.mainloop()
