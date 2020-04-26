
from pyautocad import Autocad, APoint
import tkinter
import tkinter as tk
from tkinter import *
import os


def fno_of_og1():
    global outloopy1
    global outloopx1
    global lv1
    global bt1
    global bt3
    global no_of_og1
    bt1.destroy()
    if lv1 > 0:
        lv2 = 0
        while lv2 < no_of_og1:
            globals()['fpopupMenu1%i' % lv2].destroy()
            globals()['flb1%i' % lv2].destroy()
            lv2 = lv2 + 1
        bt3.destroy()
        lv1 = 0
        outloopy1 = 100
        outloopx1 = 100
    no_of_og1 = int(sb1.get())
    while lv1 < no_of_og1:
        globals()['ftkvar1%i' % lv1] = StringVar(tkv)
        globals()['fpopupMenu1%i' % lv1] = OptionMenu(tkv, globals()['ftkvar1%i' % lv1], *choices_og)
        globals()['fpopupMenu1%i' % lv1].place(x=outloopx1, y=outloopy1)
        globals()['flb1%i' % lv1] = tk.Label(tkv, text='Outgoing - '+str(lv1+1))
        globals()['flb1%i' % lv1].place(x=outloopx1-100, y=outloopy1)
        outloopy1 = outloopy1+50
        lv1 = lv1+1
        if lv1 % 12 == 0:
            outloopx1 = outloopx1 + 300
            outloopy1 = 100

    if no_of_og1 > 0:
        bt3 = Button(tkv, text='CONFIRM', command=fconfirm)  # Bt3 for Confirm
        bt3.place(x=1000, y=50)


def fno_of_og2():
    global outloopy2
    global outloopx2
    global lv3
    global bt1
    global bt3
    global no_of_og2
    bt1.destroy()
    if lv3 > 0:
        lv4 = 0
        while lv4 < no_of_og2:
            globals()['fpopupMenu2%i' % lv4].destroy()
            globals()['flb2%i' % lv4].destroy()
            lv4 = lv4 + 1
        bt3.destroy()
        lv3 = 0
        outloopy2 = 100
        outloopx2 = 800
    no_of_og2 = int(sb2.get())
    while lv3 < no_of_og2:
        globals()['ftkvar2%i' % lv3] = StringVar(tkv)
        globals()['fpopupMenu2%i' % lv3] = OptionMenu(tkv, globals()['ftkvar2%i' % lv3], *choices_og)
        globals()['fpopupMenu2%i' % lv3].place(x=outloopx2, y=outloopy2)
        globals()['flb2%i' % lv3] = tk.Label(tkv, text='Outgoing - '+str(lv3+1))
        globals()['flb2%i' % lv3].place(x=outloopx2-100, y=outloopy2)
        outloopy2 = outloopy2+50
        lv3 = lv3+1
        if lv3 % 12 == 0:
            outloopx2 = outloopx2 + 300
            outloopy2 = 100

    if no_of_og2 > 0:
        bt3 = Button(tkv, text='CONFIRM', command=fconfirm)  # Bt3 for Confirm
        bt3.place(x=1000, y=50)


def fconfirm():
    global bt1
    global choices_og
    global og_ratings1
    global og_ratings2
    bt1.destroy()
    og_ratings1 = []
    og_ratings2 = []
    lv2 = 0
    lv4 = 0
    while lv2 < no_of_og1:
        og_ratings1.append(globals()['ftkvar1%s' % lv2].get())
        lv2 = lv2+1
    while lv4 < no_of_og2:
        og_ratings2.append(globals()['ftkvar2%s' % lv4].get())
        lv4 = lv4+1
    bt1 = Button(tkv, text="plot", command=plot)
    bt1.place(x=1100, y=50)

def fsel1(amps, breakertype, no_of_poles, ic_og):
    global p1
    global x
    global y
    global og_ratings1
    if amps == 2500 and breakertype == 'ACB BC':
            x = x - 1200
    elif amps == 1600 and breakertype == 'ACB BC':
            x = x - 1100
    elif amps == 2500 and no_of_poles == 4:
        x = x - 800
    elif (amps == 2500 and no_of_poles == 3) or (amps == 1600 and no_of_poles == 4):
        x = x - 700
    elif (amps == 1600 and no_of_poles == 3) or (amps == 1000 and no_of_poles == 4):
        x = x - 600
    elif (amps == 1000 and no_of_poles == 3) or ((amps == 630 or amps == 400) and no_of_poles == 4):
        x = x - 500
    else:
        x = x - 400
    p1 = APoint(x, y)
    acad.model.InsertBlock(p1, cwd + os.path.join(r"\Autocad Block", str(amps) + 'A ' + breakertype + ' '
                                                  + str(no_of_poles) + 'P' + ".dwg"), 1, 1, 1, 0)
    if ic_og == 'og':
        og_ratings1.remove(str(amps) + 'A ' + str(no_of_poles) + 'P ' + breakertype)


def fsel2(amps, breakertype, no_of_poles, ic_og):
    global p1
    global x
    global y
    global og_ratings2
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
        og_ratings2.remove(str(amps) + 'A ' + str(no_of_poles) + 'P ' + breakertype)


def plot():
    acad.doc.SendCommand("_AI_SELALL\n")
    acad.doc.SendCommand("_.erase\n\n")
    global x
    global y
    x = 0
    y = 0

    #For og_ratings2 plot
    sel_ic2 = tkvar3.get()
    if sel_ic2 == '2500A 4P ACB':
        fsel2(2500, "ACB", 4, 'ic')
    if sel_ic2 == '2500A 3P ACB':
        fsel2(2500, "ACB", 3, 'ic')
    if sel_ic2 == '1600A 4P ACB':
        fsel2(1600, "ACB", 4, 'ic')
    if sel_ic2 == '1600A 3P ACB':
        fsel2(1600, "ACB", 3, 'ic')
    if sel_ic2 == '1000A 4P MCCB':
        fsel2(1000, "MCCB", 4, 'ic')
    if sel_ic2 == '1000A 3P MCCB':
        fsel2(1000, "MCCB", 3, 'ic')
    if sel_ic2 == '630A 4P MCCB':
        fsel2(630, "MCCB", 4, 'ic')
    if sel_ic2 == '630A 3P MCCB':
        fsel2(630, "MCCB", 3, 'ic')
    if sel_ic2 == '400A 4P MCCB':
        fsel2(400, "MCCB", 4, 'ic')
    if sel_ic2 == '400A 3P MCCB':
        fsel2(400, "MCCB", 3, 'ic')
    if sel_ic2 == 'UP TO 250A 4P MCCB':
        fsel2(250, "MCCB", 4, 'ic')
    if sel_ic2 == 'UP TO 250A 3P MCCB':
        fsel2(250, "MCCB", 3, 'ic')

    def cycle1():
        global og_ratings2
        global p1
        global x
        global y
        if "2500A 4P ACB" in og_ratings2:
            fsel2(2500, "ACB", 4, 'og')
            cycle1()
        elif "2500A 3P ACB" in og_ratings2:
            fsel2(2500, "ACB", 3, 'og')
            cycle1()
        elif "1600A 4P ACB" in og_ratings2:
            fsel2(1600, "ACB", 4, 'og')
            cycle1()
        elif "1600A 3P ACB" in og_ratings2:
            fsel2(1600, "ACB", 3, 'og')
            cycle1()
        elif "1000A 4P MCCB" in og_ratings2:
            fsel2(1000, "MCCB", 4, 'og')
            cycle1()
        elif "1000A 3P MCCB" in og_ratings2:
            fsel2(1000, "MCCB", 3, 'og')
            cycle1()
        elif "630A 4P MCCB VER" in og_ratings2:
            fsel2(630, "MCCB VER", 4, 'og')
            cycle1()
        elif "630A 3P MCCB VER" in og_ratings2:
            fsel2(630, "MCCB VER", 3, 'og')
            cycle1()
        elif "400A 4P MCCB VER" in og_ratings2:
            fsel2(400, "MCCB VER", 4, 'og')
            cycle1()
        elif "400A 3P MCCB VER" in og_ratings2:
            fsel2(400, "MCCB VER", 3, 'og')
            cycle1()
        else:
            if "630A 4P MCCB HOR" in og_ratings2:
                if y < 700:
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 4MODULE.dwg", 1, 1, 1, 0)
                og_ratings2.remove("630A 4P MCCB HOR")
                y = y-400
                if y < 700:
                    x = x+700
                    y = 0
                cycle1()
            if "630A 3P MCCB HOR" in og_ratings2:
                if y < 700:
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 4MODULE.dwg", 1, 1, 1, 0)
                og_ratings2.remove("630A 3P MCCB HOR")
                y = y-400
                if y < 700:
                    x = x+700
                    y = 0
                cycle1()
            if "400A 4P MCCB" in og_ratings2:
                if y < 700:
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 4MODULE.dwg", 1, 1, 1, 0)
                og_ratings2.remove("400A 4P MCCB")
                y = y-400
                if y < 700:
                    x = x+700
                    y = 0
                cycle1()
            elif "400A 3P MCCB" in og_ratings2:
                check1 = y-300
                if check1 == 400:
                    i = 0
                    while i < 2:
                        i = i+1
                        if "UP TO 250A 3P MCCB" in og_ratings2 and y >= 500:
                            p1 = APoint(x, y)
                            acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                            og_ratings2.remove("UP TO 250A 3P MCCB")
                            y = y - 200
                            if y < 500:
                                x = x + 700
                                y = 0
                        elif "UP TO 250A 4P MCCB" in og_ratings2 and y >= 500:
                            p1 = APoint(x, y)
                            acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                            og_ratings2.remove("UP TO 250A 4P MCCB")
                            y = y - 200
                            if y < 500:
                                x = x + 700
                                y = 0
                        else:
                            if y >= 600:
                                p1 = APoint(x, y)
                                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 3MODULE.dwg", 1, 1, 1, 0)
                                og_ratings2.remove("400A 3P MCCB")
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
                    og_ratings2.remove("400A 3P MCCB")
                    y = y-300

                    if "UP TO 250A 3P MCCB" in og_ratings2 and y == 500:
                        p1 = APoint(x, y)
                        acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                        og_ratings2.remove("UP TO 250A 3P MCCB")
                        y = y - 200
                    elif "UP TO 250A 4P MCCB" in og_ratings2 and y == 500:
                        p1 = APoint(x, y)
                        acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                        og_ratings2.remove("UP TO 250A 4P MCCB")
                    if y < 600:
                        x = x+700
                        y = 0
                    cycle1()
            elif "UP TO 250A 4P MCCB" in og_ratings2:
                if y < 500:
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                og_ratings2.remove("UP TO 250A 4P MCCB")
                y = y-200
                if y < 500:
                    x = x+700
                    y = 0
                cycle1()
            elif "UP TO 250A 3P MCCB" in og_ratings2:
                if y < 500:
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                og_ratings2.remove("UP TO 250A 3P MCCB")
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


    # For og_ratings1 plot
    x = 0
    y = 0
    sel_bc = tkvar2.get()
    if sel_bc == '2500A 4P ACB':
        fsel1(2500, "ACB BC", 4, 'ic')
    if sel_bc == '1600A 4P ACB':
        fsel1(2500, "ACB BC", 4, 'ic')
    sel_ic1 = tkvar1.get()
    if sel_ic1 == '2500A 4P ACB':
        fsel1(2500, "ACB", 4, 'ic')
    if sel_ic1 == '2500A 3P ACB':
        fsel1(2500, "ACB", 3, 'ic')
    if sel_ic1 == '1600A 4P ACB':
        fsel1(1600, "ACB", 4, 'ic')
    if sel_ic1 == '1600A 3P ACB':
        fsel1(1600, "ACB", 3, 'ic')
    if sel_ic1 == '1000A 4P MCCB':
        fsel1(1000, "MCCB", 4, 'ic')
    if sel_ic1 == '1000A 3P MCCB':
        fsel1(1000, "MCCB", 3, 'ic')
    if sel_ic1 == '630A 4P MCCB':
        fsel1(630, "MCCB", 4, 'ic')
    if sel_ic1 == '630A 3P MCCB':
        fsel1(630, "MCCB", 3, 'ic')
    if sel_ic1 == '400A 4P MCCB':
        fsel1(400, "MCCB", 4, 'ic')
    if sel_ic1 == '400A 3P MCCB':
        fsel1(400, "MCCB", 3, 'ic')
    if sel_ic1 == 'UP TO 250A 4P MCCB':
        fsel1(250, "MCCB", 4, 'ic')
    if sel_ic1 == 'UP TO 250A 3P MCCB':
        fsel1(250, "MCCB", 3, 'ic')

    def cycle2():
        global og_ratings1
        global p1
        global x
        global y
        if "2500A 4P ACB" in og_ratings1:
            fsel1(2500, "ACB", 4, 'og')
            cycle2()
        elif "2500A 3P ACB" in og_ratings1:
            fsel1(2500, "ACB", 3, 'og')
            cycle2()
        elif "1600A 4P ACB" in og_ratings1:
            fsel1(1600, "ACB", 4, 'og')
            cycle2()
        elif "1600A 3P ACB" in og_ratings1:
            fsel1(1600, "ACB", 3, 'og')
            cycle2()
        elif "1000A 4P MCCB" in og_ratings1:
            fsel1(1000, "MCCB", 4, 'og')
            cycle2()
        elif "1000A 3P MCCB" in og_ratings1:
            fsel1(1000, "MCCB", 3, 'og')
            cycle2()
        elif "630A 4P MCCB VER" in og_ratings1:
            fsel1(630, "MCCB VER", 4, 'og')
            cycle2()
        elif "630A 3P MCCB VER" in og_ratings1:
            fsel1(630, "MCCB VER", 3, 'og')
            cycle2()
        elif "400A 4P MCCB VER" in og_ratings1:
            fsel1(400, "MCCB VER", 4, 'og')
            cycle2()
        elif "400A 3P MCCB VER" in og_ratings1:
            fsel1(400, "MCCB VER", 3, 'og')
            cycle2()
        else:
            if "630A 4P MCCB HOR" in og_ratings1:
                if y < 700:
                    x = x-700
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 4MODULE.dwg", 1, 1, 1, 0)
                og_ratings1.remove("630A 4P MCCB HOR")
                y = y-400
                if y < 700:
                    y = 0
                cycle2()
            if "630A 3P MCCB HOR" in og_ratings1:
                if y < 700:
                    x = x-700
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 4MODULE.dwg", 1, 1, 1, 0)
                og_ratings1.remove("630A 3P MCCB HOR")
                y = y-400
                if y < 700:
                    y = 0
                cycle2()
            if "400A 4P MCCB" in og_ratings1:
                if y < 700:
                    x = x-700
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 4MODULE.dwg", 1, 1, 1, 0)
                og_ratings1.remove("400A 4P MCCB")
                y = y-400
                if y < 700:
                    y = 0
                cycle2()
            elif "400A 3P MCCB" in og_ratings1:
                check1 = y-300
                if check1 == 400:
                    i = 0
                    while i < 2:
                        i = i+1
                        if "UP TO 250A 3P MCCB" in og_ratings1 and y >= 500:
                            p1 = APoint(x, y)
                            acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                            og_ratings1.remove("UP TO 250A 3P MCCB")
                            y = y - 200
                            if y < 500:
                                y = 0
                        elif "UP TO 250A 4P MCCB" in og_ratings1 and y >= 500:
                            p1 = APoint(x, y)
                            acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                            og_ratings1.remove("UP TO 250A 4P MCCB")
                            y = y - 200
                            if y < 500:
                                y = 0
                        else:
                            if y >= 600:
                                p1 = APoint(x, y)
                                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 3MODULE.dwg", 1, 1, 1, 0)
                                og_ratings1.remove("400A 3P MCCB")
                            if y < 600:
                                y = 0
                    cycle2()
                else:
                    if y < 600:
                        x = x-700
                        p1 = APoint(x, y)
                        acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                        y = 1900
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 3MODULE.dwg", 1, 1, 1, 0)
                    og_ratings1.remove("400A 3P MCCB")
                    y = y-300

                    if "UP TO 250A 3P MCCB" in og_ratings1 and y == 500:
                        p1 = APoint(x, y)
                        acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                        og_ratings1.remove("UP TO 250A 3P MCCB")
                        y = y - 200
                    elif "UP TO 250A 4P MCCB" in og_ratings1 and y == 500:
                        p1 = APoint(x, y)
                        acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                        og_ratings1.remove("UP TO 250A 4P MCCB")
                    if y < 600:
                        y = 0
                    cycle2()
            elif "UP TO 250A 4P MCCB" in og_ratings1:
                if y < 500:
                    x = x-700
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                og_ratings1.remove("UP TO 250A 4P MCCB")
                y = y-200
                if y < 500:
                    y = 0
                cycle2()
            elif "UP TO 250A 3P MCCB" in og_ratings1:
                if y < 500:
                    x = x-700
                    p1 = APoint(x, y)
                    acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W CUBICLE.dwg", 1, 1, 1, 0)
                    y = 1900
                p1 = APoint(x, y)
                acad.model.InsertBlock(p1, cwd + r"\Autocad Block\700W 2MODULE.dwg", 1, 1, 1, 0)
                og_ratings1.remove("UP TO 250A 3P MCCB")
                y = y-200
                if y < 500:
                    y = 0
                cycle2()
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
    cycle2()





# Global Variables Declaration
choices_ic = ['2500A 4P ACB', '2500A 3P ACB', '1600A 4P ACB', '1600A 3P ACB',
              '1000A 4P MCCB', '1000A 3P MCCB', '630A 4P MCCB', '630A 3P MCCB',
              '400A 4P MCCB', '400A 3P MCCB', 'UP TO 250A 4P MCCB', 'UP TO 250A 3P MCCB'
              ]

choices_bc = ['2500A 4P ACB', '1600A 4P ACB']

choices_og = ['2500A 4P ACB', '2500A 3P ACB', '1600A 4P ACB', '1600A 3P ACB',
              '1000A 4P MCCB', '1000A 3P MCCB', '630A 4P MCCB VER', '630A 3P MCCB VER',
              '630A 4P MCCB HOR', '630A 3P MCCB HOR', '400A 4P MCCB', '400A 3P MCCB',
              'UP TO 250A 4P MCCB', 'UP TO 250A 3P MCCB'
              ]

outloopx1 = 100
outloopy1 = 100
outloopx2 = 800
outloopy2 = 100
x = 0
y = 0
lv1 = 0
lv3 = 0
og_ratings1 = []
og_ratings2 = []
cwd = os.getcwd()
p1 = APoint(x, y)

# Opening AutoCAD
acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python")


# Opening tkinter Window
tkv = tkinter.Tk()
tkv.state('zoomed')
tkv.title("Enclosure Design")

tkvar1 = StringVar(tkv)
tkvar2 = StringVar(tkv)
tkvar3 = StringVar(tkv)

lb1 = tk.Label(tkv, text='Select Incomer 1 - ')
lb1.place(x=0, y=5)

lb3 = tk.Label(tkv, text='Select Bus Coupler - ')
lb3.place(x=280, y=5)

lb4 = tk.Label(tkv, text='Select Incomer 2 - ')
lb4.place(x=700, y=5)


# Popup Menu for Incomer-1 rating
popupMenu1 = OptionMenu(tkv, tkvar1, *choices_ic)
popupMenu1.place(x=100, y=0)
ic_rating1 = tkvar1.get()

# Popup Menu for Bus Coupler rating
popupMenu2 = OptionMenu(tkv, tkvar2, *choices_bc)
popupMenu2.place(x=390, y=0)
bc_rating = tkvar2.get()

# Popup Menu for Incomer-2 rating
popupMenu3 = OptionMenu(tkv, tkvar3, *choices_ic)
popupMenu3.place(x=800, y=0)
ic_rating2 = tkvar3.get()


# Spinbox for no. of outgoings-Incomer 1
lb2 = tk.Label(tkv, text='No of outgoings - ')
lb2.place(x=0, y=50)
sb1 = tk.Spinbox(tkv, from_=0, to=50)
sb1.place(x=100, y=50)

# Spinbox for no. of outgoings-Incomer 2
lb5 = tk.Label(tkv, text='No of outgoings - ')
lb5.place(x=700, y=50)
sb2 = tk.Spinbox(tkv, from_=0, to=50)
sb2.place(x=800, y=50)

# Buttons : bt1 - plot, bt2 - OK (For No of outgoings - Incoming 1)
bt1 = Button(tkv, text="plot", command=plot)
bt2 = Button(tkv, text='OK', command=fno_of_og1)
bt2.place(x=250, y=50)

# Buttons : bt4 - OK (For No of outgoings - Incoming 2)
bt4 = Button(tkv, text='OK', command=fno_of_og2)
bt4.place(x=950, y=50)


tk.mainloop()
