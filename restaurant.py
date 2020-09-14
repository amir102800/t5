import tkinter as tk
import tkinter.ttk as ttk






root = tk.Tk()





note = ttk.Notebook()
note.grid(row=0, column=0)
drink = tk.Frame()
food = tk.Frame()
reciept=tk.Frame()
note.add(drink, text='drink')
note.add(food, text='food')
note.add(reciept, text='reciept')







root.mainloop()