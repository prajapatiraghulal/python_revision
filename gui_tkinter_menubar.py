import tkinter
from tkinter import  ttk
import  tkinter as tk
from typing import Text

win = tk.Tk()

def func():
    print('called')
# # # # #simple menu  ---------------------------------------------------------------simple menu-------------------------------------------
# # # # menu_bar = tk.Menu(win)
# # # # menu_bar.add_command(label='file',command=func)
# # # # menu_bar.add_command(label='edit',command=func)
# # # # menu_bar.add_command(label='help',command=func)

####--------------------------------------------------------------dropdown menu ---------------------------
main_menu = tk.Menu(win)

file_menu = tk.Menu(main_menu,tearoff=False)
file_menu.add_command(label='open',command=func)
file_menu.add_command(label='save',command=func)
file_menu.add_separator()
file_menu.add_command(label='save as',command=func)

edit_menu = tk.Menu(main_menu,tearoff=False)
edit_menu.add_command(label='select ',command=func)
edit_menu.add_command(label='deselect',command=func)
help_menu = tk.Menu(main_menu,tearoff=False)
help_menu.add_command(label='help?',command=func)


main_menu.add_cascade(label='file',menu=file_menu)
main_menu.add_cascade(label='edit',menu=edit_menu)
main_menu.add_cascade(label='help',menu=help_menu)





win.config(menu=main_menu)
win.mainloop()