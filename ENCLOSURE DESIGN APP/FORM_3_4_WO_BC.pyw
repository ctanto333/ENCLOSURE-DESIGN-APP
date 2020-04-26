
from pyautocad import Autocad, APoint
import tkinter
import tkinter as tk
from tkinter import *
import os


def fno_of_og():
    global outloopy
    global outloopx
    global lv1
    global bt1
    global bt3
    global no_of_og
    bt1.destroy()
    if lv1 > 0:
        lv2 = 0
        while lv2 < no_of_og:
            globals()['fpopupMenu%i' % lv2].destroy()
            globals()['flb%i' % lv2].destroy()
            lv2 = lv2 + 1
        bt3.destroy()
        lv1 = 0
        outloopy = 100
        outloopx = 100
    no_of_og = int(sb1.get())
    while lv1 < no_of_og:
        globals()['ftkvar%i' % lv1] = StringVar(tkv)
        globals()['fpopupMenu%i' % lv1] = OptionMenu(tkv, globals()['ftkvar%i' % lv1], *choices_og)
        globals()['fpopupMenu%i' % lv1].place(x=outloopx, y=outloopy)
        globals()['flb%i' % lv1] = tk.Label(tkv, text='Outgoing - '+str(lv1+1))
        globals()['flb%i' % lv1].place(x=outloopx-100, y=outloopy)
        outloopy = outloopy+50
        lv1 = lv1+1
        if lv1 % 12 == 0:
            outloopx = outloopx + 300
            outloopy = 100

    if no_of_og > 0:
        bt3 = Button(tkv, text='CONFIRM', command=fconfirm)
        bt3.pack()


def fconfirm():
    global bt1
    global choices_og
    global og_ratings
    bt1.destroy()
    og_ratings = []
    lv2 = 0
    while lv2 < no_of_og:
        og_ratings.append(globals()['ftkvar%s' % lv2].get())
        lv2 = lv2+1
    bt1 = Button(tkv, text="plot", command=plot)
    bt1.pack()


def fsel(amps, breakertype, no_of_poles, ic_og):
    global p1
    global x
    global y
    global og_ratings
    p1 = APoint(x, y)
    acad.model.InsertBlock(p1, cwd + os.path.join(r"\Autocad Block", str(amps) + 'A ' + breakertype + ' '
                                                  + str(no_of_poles) + 'P' + ".dwg"), 1, 1, 1, 0)
    if amps == 2500 and no_of_poles == 4:
        x = x + 800
    elif (amps == 2500 and no_of_poles == 3) or (amps == 1600 and no_of_poles == 4):
        x = x + 700
    elif (amps == 1600 and no_of_poles == 3) or (amps == 1000 and no_of_poles == 4):
        x = x + 600
    elif (amps == 1000 and no_of_poles == 3) or ((amps == 630 or amps == 400) and no_of_poles == 4):
        x = x + 500
    else:
        x = x + 400
    if ic_og == 'og':
        og_ratings.remove(str(amps) + 'A ' + str(no_of_poles) + 'P ' + breakertype)


def plot():
    acad.doc.SendCommand("_AI_SELALL\n")
    acad.doc.SendCommand("_.erase\n\n")
    global x
    global y
    x = 0
    y = 0
    sel = tkvar.get()
    if sel == '2500A 4P ACB':
        fsel(2500, "ACB", 4, 'ic')
    if sel == '2500A 3P ACB':
        fsel(2500, "ACB", 3, 'ic')
    if sel == '1600A 4P ACB':
        fsel(1600, "ACB", 4, 'ic')
    if sel == '1600A 3P ACB':
        fsel(1600, "ACB", 3, 'ic')
    if sel == '1000A 4P MCCB':
        fsel(1000, "MCCB", 4, 'ic')
    if sel == '1000A 3P MCCB':
        fsel(1000, "MCCB", 3, 'ic')
    if sel == '630A 4P MCCB':
        fsel(630, "MCCB", 4, 'ic')
    if sel == '630A 3P MCCB':
        fsel(630, "MCCB", 3, 'ic')
    if sel == '400A 4P MCCB':
        fsel(400, "MCCB", 4, 'ic')
    if sel == '400A 3P MCCB':
        fsel(400, "MCCB", 3, 'ic')
    if sel == 'UP TO 250A 4P MCCB':
        fsel(250, "MCCB", 4, 'ic')
    if sel == 'UP TO 250A 3P MCCB':
        fsel(250, "MCCB", 3, 'ic')

    def cycle1():
        global og_ratings
        global p1
        global x
        global y
        if "2500A 4P ACB" in og_ratings:
            fsel(2500, "ACB", 4, 'og')
            cycle1()
        elif "2500A 3P ACB" in og_ratings:
            fsel(2500, "ACB", 3, 'og')
            cycle1()
        elif "1600A 4P ACB" in og_ratings:
            fsel(1600, "ACB", 4, 'og')
            cycle1()
        elif "1600A 3P ACB" in og_ratings:
            fsel(1600, "ACB", 3, 'og')
            cycle1()
        elif "1000A 4P MCCB" in og_ratings:
            fsel(1000, "MCCB", 4, 'og')
            cycle1()
        elif "1000A 3P MCCB" in og_ratings:
            fsel(1000, "MCCB", 3, 'og')
            cycle1()
        elif "630A 4P MCCB VER" in og_ratings:
            fsel(630, "MCCB VER", 4, 'og')
            cycle1()
        elif "630A 3P MCCB VER" in og_ratings:
            fsel(630, "MCCB VER", 3, 'og')
            cycle1()
        elif "400A 4P MCCB VER" in og_ratings:
            fsel(400, "MCCB VER", 4, 'og')
            cycle1()
        elif "400A 3P MCCB VER" in og_ratings:
            fsel(400, "MCCB VER", 3, 'og')
            cycle1()
        else:
            if "630A 4P MCCB HOR" in og_ratings:
                if y < 700:
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 4MODULE.dwg", 1, 1, 1, 0)
                og_ratings.remove("630A 4P MCCB HOR")
                y = y-400
                if y < 700:
                    x = x+700
                    y = 0
                cycle1()
            if "630A 3P MCCB HOR" in og_ratings:
                if y < 700:
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 4MODULE.dwg", 1, 1, 1, 0)
                og_ratings.remove("630A 3P MCCB HOR")
                y = y-400
                if y < 700:
                    x = x+700
                    y = 0
                cycle1()
            if "400A 4P MCCB" in og_ratings:
                if y < 700:
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 4MODULE.dwg", 1, 1, 1, 0)
                og_ratings.remove("400A 4P MCCB")
                y = y-400
                if y < 700:
                    x = x+700
                    y = 0
                cycle1()
            elif "400A 3P MCCB" in og_ratings:
                check1 = y-300
                if check1 == 400:
                    i = 0
                    while i < 2:
                        i = i+1
                        if "UP TO 250A 3P MCCB" in og_ratings and y >= 500:
                            p1 = APoint(x, y)
                            acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                            og_ratings.remove("UP TO 250A 3P MCCB")
                            y = y - 200
                            if y < 500:
                                x = x + 700
                                y = 0
                        elif "UP TO 250A 4P MCCB" in og_ratings and y >= 500:
                            p1 = APoint(x, y)
                            acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                            og_ratings.remove("UP TO 250A 4P MCCB")
                            y = y - 200
                            if y < 500:
                                x = x + 700
                                y = 0
                        else:
                            if y >= 600:
                                p1 = APoint(x, y)
                                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 3MODULE.dwg", 1, 1, 1, 0)
                                og_ratings.remove("400A 3P MCCB")
                            if y < 600:
                                x = x + 700
                                y = 0
                    cycle1()
                else:
                    if y < 600:
                        p1 = APoint(x, y)
                        acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                        y = 1900
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 3MODULE.dwg", 1, 1, 1, 0)
                    og_ratings.remove("400A 3P MCCB")
                    y = y-300

                    if "UP TO 250A 3P MCCB" in og_ratings and y == 500:
                        p1 = APoint(x, y)
                        acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                        og_ratings.remove("UP TO 250A 3P MCCB")
                        y = y - 200
                    elif "UP TO 250A 4P MCCB" in og_ratings and y == 500:
                        p1 = APoint(x, y)
                        acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                        og_ratings.remove("UP TO 250A 4P MCCB")
                    if y < 600:
                        x = x+700
                        y = 0
                    cycle1()
            elif "UP TO 250A 4P MCCB" in og_ratings:
                if y < 500:
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                og_ratings.remove("UP TO 250A 4P MCCB")
                y = y-200
                if y < 500:
                    x = x+700
                    y = 0
                cycle1()
            elif "UP TO 250A 3P MCCB" in og_ratings:
                if y < 500:
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                og_ratings.remove("UP TO 250A 3P MCCB")
                y = y-200
                if y < 500:
                    x = x+700
                    y = 0
                cycle1()
            else:
                while y >= 500:
                    if y == 600:
                        p1 = APoint(x, y)
                        acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 3BLANK.dwg", 1, 1, 1, 0)
                        y = y-300
                    else:
                        p1 = APoint(x, y)
                        acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2BLANK.dwg", 1, 1, 1, 0)
                        y = y-200
    cycle1()




# Global Variables Declaration
choices_ic = ['2500A 4P ACB', '2500A 3P ACB', '1600A 4P ACB', '1600A 3P ACB',
              '1000A 4P MCCB', '1000A 3P MCCB', '630A 4P MCCB', '630A 3P MCCB',
              '400A 4P MCCB', '400A 3P MCCB', 'UP TO 250A 4P MCCB', 'UP TO 250A 3P MCCB'
              ]

choices_og = ['2500A 4P ACB', '2500A 3P ACB', '1600A 4P ACB', '1600A 3P ACB',
              '1000A 4P MCCB', '1000A 3P MCCB', '630A 4P MCCB VER', '630A 3P MCCB VER',
              '630A 4P MCCB HOR', '630A 3P MCCB HOR', '400A 4P MCCB', '400A 3P MCCB',
              'UP TO 250A 4P MCCB', 'UP TO 250A 3P MCCB'
              ]

outloopx = 100
outloopy = 100
x = 0
y = 0
lv1 = 0
og_ratings = []
cwd = os.getcwd()
p1 = APoint(x, y)

# Opening AutoCAD
acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python")

# Opening tkinter Window
tkv = tkinter.Tk()
tkv.state('zoomed')
tkv.title("Enclosure Design")

tkvar = StringVar(tkv)
lb1 = tk.Label(tkv, text='Select Incomer 1 - ')
lb1.place(x=0, y=5)


# Popup Menu for Incomer rating
popupMenu1 = OptionMenu(tkv, tkvar, *choices_ic)
popupMenu1.place(x=100, y=0)
ic_rating1 = tkvar.get()

# Spinbox for no. of outgoings
lb2 = tk.Label(tkv, text='No of outgoings - ')
lb2.place(x=0, y=50)
sb1 = tk.Spinbox(tkv, from_=0, to=50)
sb1.place(x=100, y=50)

# Buttons : bt1 - plot, bt2 - OK (For No of outgoings)
bt1 = Button(tkv, text="plot", command=plot)
bt2 = Button(tkv, text='OK', command=fno_of_og)
bt2.place(x=250, y=50)


tk.mainloop()
