from ttkfun import *
import ttkfun
from tkinter import ttk
global op
op = ''
def chng():
    msgbox('askyesno', 'changing', 'do you wanna change the calculator to a teacher calculator')
    j = ttkfun.i
    if j == True:
        win.destroy()

        def equ():
            try:
                global op
                sum = eval(op)
                e = 20-sum
                s = str(e)
                vr.set(s)
            except:
                msgbox('showerror', 'error', 'an error has occurred')
        def click(num):
            try:
                global op
                op = op + str(num)
                vr.set(op)
            except:
                msgbox('showerror', 'error', 'an error has occurred')
        def clear():
            try:
                global op
                op = ''
                vr.set(op)
            except:
                msgbox('showerror', 'error', 'an error has occurred')
        try:
            win2 = Tk()
            win2.title('Teacher Calculator')
            vr = StringVar()
            en = ttk.Entry(win2, textvariable=vr)
            en.focus()
            en.pack()
            frame = Frame()
            frame.pack()
            ttk.Button(frame, text='0.25', command=lambda: click(0.25)).grid(row=0, column=0)
            ttk.Button(frame, text='0.75', command=lambda: click(0.75)).grid(row=0, column=1)
            ttk.Button(frame, text='0.5', command=lambda: click(0.5)).grid(row=0, column=2)
            ttk.Button(frame, text='+', command=lambda: click('+')).grid(row=0, column=3)
            ttk.Button(frame, text='1', command=lambda: click(1)).grid(row=1, column=0)
            ttk.Button(frame, text='2', command=lambda: click(2)).grid(row=1, column=1)
            ttk.Button(frame, text='3', command=lambda: click(3)).grid(row=1, column=2)
            ttk.Button(frame, text='-', command=lambda: click('-')).grid(row=1, column=3)
            ttk.Button(frame, text='4', command=lambda: click(4)).grid(row=2, column=0)
            ttk.Button(frame, text='5', command=lambda: click(5)).grid(row=2, column=1)
            ttk.Button(frame, text='6', command=lambda: click(6)).grid(row=2, column=2)
            ttk.Button(frame, text='*', command=lambda: click('*')).grid(row=2, column=3)
            ttk.Button(frame, text='7', command=lambda: click(7)).grid(row=3, column=0)
            ttk.Button(frame, text='8', command=lambda: click(8)).grid(row=3, column=1)
            ttk.Button(frame, text='9', command=lambda: click(9)).grid(row=3, column=2)
            ttk.Button(frame, text='/', command=lambda: click('/')).grid(row=3, column=3)
            ttk.Button(frame, text='0', command=lambda: click(0)).grid(row=4, column=0)
            ttk.Button(frame, text='=', command=equ).grid(row=4, column=1)
            ttk.Button(frame, text='c', command=clear).grid(row=4, column=2)
            ttk.Button(frame, text='exit', command=win2.quit).grid(row=4, column=3)

            win2.mainloop()
        except:
            msgbox('showerror', 'error', 'an error has occurred')
    else:
        pass
def equ():
    try:
        global op
        sum = str(eval(op))
        vr.set(sum)
    except:
        msgbox('showerror', 'error', 'an error has occurred')
def click(num):
    try:
        global op
        op = op+str(num)
        vr.set(op)
    except:
        msgbox('showerror', 'error', 'an error has occurred')
def clear():
    try:
        global op
        op = ''
        vr.set(op)
    except:
        msgbox('showerror', 'error', 'an error has occurred')
try:
    win = Tk()
    win.title('Calculator')
    vr = StringVar()
    en = ttk.Entry(win, textvariable=vr)
    en.focus()
    en.pack()
    frame = Frame()
    frame.pack()
    ttk.Button(frame, text='0.25', command=lambda :click(0.25)).grid(row=0, column=0)
    ttk.Button(frame, text='0.75', command=lambda :click(0.75)).grid(row=0, column=1)
    ttk.Button(frame, text='0.5', command=lambda :click(0.5)).grid(row=0, column=2)
    ttk.Button(frame, text='+', command=lambda :click('+')).grid(row=0, column=3)
    ttk.Button(frame, text='1', command=lambda :click(1)).grid(row=1, column=0)
    ttk.Button(frame, text='2', command=lambda :click(2)).grid(row=1, column=1)
    ttk.Button(frame, text='3', command=lambda :click(3)).grid(row=1, column=2)
    ttk.Button(frame, text='-', command=lambda :click('-')).grid(row=1, column=3)
    ttk.Button(frame, text='4', command=lambda :click(4)).grid(row=2, column=0)
    ttk.Button(frame, text='5', command=lambda :click(5)).grid(row=2, column=1)
    ttk.Button(frame, text='6', command=lambda :click(6)).grid(row=2, column=2)
    ttk.Button(frame, text='*', command=lambda :click('*')).grid(row=2, column=3)
    ttk.Button(frame, text='7', command=lambda :click(7)).grid(row=3, column=0)
    ttk.Button(frame, text='8', command=lambda :click(8)).grid(row=3, column=1)
    ttk.Button(frame, text='9', command=lambda :click(9)).grid(row=3, column=2)
    ttk.Button(frame, text='/', command=lambda :click('/')).grid(row=3, column=3)
    ttk.Button(frame, text='0', command=lambda :click(0)).grid(row=4, column=0)
    ttk.Button(frame, text='=', command=equ).grid(row=4, column=1)
    ttk.Button(frame, text='c', command=clear).grid(row=4, column=2)
    ttk.Button(frame, text='change', command=chng).grid(row=4, column=3)
    win.mainloop()
except:
    msgbox('showerror', 'error', 'an error has occurred')