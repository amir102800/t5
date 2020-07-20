import tkinter as tk
from datetime import datetime


def turn():
    global n
    n += 1
    numbers.append(n + 1)
    print(numbers)
    d = datetime.now()
    a3.config(text=d.strftime('%c'))
    a2.config(text=numbers[-1])


def op1():
    if numbers:
        lo1.config(text=numbers.pop(0))


def op2():
    if numbers:
        lo2.config(text=numbers.pop(1))


def op3():
    if numbers:
        lo3.config(text=numbers.pop(2))


root = tk.Tk()
n = -1
numbers = []

a3 = tk.Label(root, text='')
a3.grid(row=0, column=0)

b1 = tk.Button(root, text='get turn !', command=turn)
b1.grid(row=1, column=0)

a2 = tk.Label(root, text='')
a2.grid(row=2, column=0)

tp = tk.Toplevel(root)
o1 = tk.Button(tp, text='operators 1 ', command=op1)
o1.grid(row=0, column=0)
o2 = tk.Button(tp, text='operators 2 ', command=op2)
o2.grid(row=0, column=1)
o3 = tk.Button(tp, text='operators 3  ', command=op3)
o3.grid(row=0, column=2)

lo1 = tk.Label(tp, text='--')
lo1.grid(row=1, column=0)
lo2 = tk.Label(tp, text='--')
lo2.grid(row=1, column=1)
lo3 = tk.Label(tp, text='--')
lo3.grid(row=1, column=2)

root.mainloop()
