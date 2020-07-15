import tkinter as tk
from datetime import datetime


def turn():
    numbers.append(len(numbers)+1)
    print(numbers)
    d = datetime.now()
    a3.config(text=d.strftime('%c'))
    a2.config(text=numbers[-1])

root = tk.Tk()

numbers=[]

a3=tk.Label(root, text= '')
a3.grid()

b1=tk.Button(root, text='get turn !', command=turn)
b1.pack()

a2=tk.Label(root, text='')
a2.pack()




root.mainloop()