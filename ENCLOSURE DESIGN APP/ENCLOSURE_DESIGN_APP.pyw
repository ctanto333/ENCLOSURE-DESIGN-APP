import tkinter
import tkinter as tk
from tkinter import *
from os import startfile
import os
cwd = os.getcwd()

def open_python(x):
    startfile(cwd + '\\' + x)

main_window = tkinter.Tk()
#main_window.state('zoomed')
main_window.geometry('300x300')
main_window.title("Enclosure Design V-0.1")

b1 = Button(main_window, text='Form3/4 W/O BC', height=2, width=20, command=lambda: open_python('FORM_3_4_WO_BC.pyw'))
b1.place(x=75, y=75)

b2 = Button(main_window, text='Form3/4 W/I BC', height=2, width=20, command=lambda: open_python('FORM_3_4_WI_BC.pyw'))
b2.place(x=75, y=175)



main_window.mainloop()
