import tkinter as tk


root = tk.Tk()

a1=tk.Label(root, text='')
a1.pack()
b1=tk.Button(root, text='get turn !', command=turn)
b1.pack()

root.mainloop()