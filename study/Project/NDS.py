import tkinter as tk
from tkinter import *
from tkinter import messagebox

def pred():
    messagebox.showinfo("Помощь", "Вводите имеющиеся данные в поле 'Сумма:'")

def validate(n_v):
    return n_v == "" or n_v.isnumeric()

def clear():
    n_entry.delete(0, END)

def calc():
    a = p.get()
    b = s.get()
    if a == 0 and b == 0:
        rez = n.get() * 1.2
    if a == 1 and b == 0:
        rez = n.get() * 1.1

    if a == 0 and b == 1:
        rez = n.get() - (n.get() / 120 * 20)
    if a == 1 and b == 1:
        rez = n.get() - (n.get() / 110 * 10)

    if a == 0 and b == 2:
        rez = n.get() + (n.get() / 0.2)
    if a == 1 and b == 2:
        rez = n.get() + (n.get() / 0.1)
    if n.get() == 0:
        messagebox.showinfo("Введите данные!")
    messagebox.showinfo("Результат", "Сумма : " + str(rez))


calculator = Tk()
x = (calculator.winfo_screenwidth() - calculator.winfo_reqwidth()) / 2
y = (calculator.winfo_screenheight() - calculator.winfo_reqheight()) / 2
calculator.wm_geometry("+%d+%d" % (x-100, y-50))
calculator.title("Калькулятор НДС")

p = StringVar()
p_label = Label(text="НДС %:").grid(row=0, column=0, sticky=W)
p = IntVar()
p.set(0)
p0 = Radiobutton(text='20%', variable=p, value=0).grid(row=0, column=1, padx=5, pady=5, sticky=W)
p1 = Radiobutton(text='10%', variable=p, value=1).grid(row=1, column=1, padx=5, pady=5, sticky=W)

s = StringVar()
s_label = Label(text="Способ вычисления:").grid(row=2, column=0, sticky=W)
s = IntVar()
s.set(0)
s0 = Radiobutton(text='Начислить НДС (прибавить НДС к сумме)', variable=s, value=0).grid(row=2, column=1, padx=5, pady=5, sticky=W)
s1 = Radiobutton(text='Выделить НДС (вычесть НДС из суммы)', variable=s, value=1).grid(row=3, column=1, padx=5, pady=5, sticky=W)
s2 = Radiobutton(text='Рассчитать сумму, зная НДС', variable=s, value=2).grid(row=4, column=1, padx=5, pady=5, sticky=W)

n = IntVar()
n.set('')
n_label = Label(text="Сумма:").grid(row=5, column=0, sticky=W)
reg = (calculator.register(validate), '%P')
n_entry = Entry(validate='key', validatecommand=reg, textvariable=n)
n_entry.grid(row=5, column=1, padx=5, pady=5, sticky=W)


help_but = Button(text="Помощь", command=pred).grid(row=0, column=3, padx=5, pady=5, sticky=W)

clear_but = Button(text="Очистить", command=clear).grid(row=5, column=3, padx=5, pady=5, sticky=W)

rez_but = Button(text="Расчитать", command=calc).grid(row=6, column=1, padx=5, pady=5, sticky=W)


calculator.mainloop()
