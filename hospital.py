import tkinter as tk
import tkinter.ttk as ttk 


timer = tk.Tk()
note = ttk.Notebook()
note.grid(row=0 , column=0)

timer = tk.Frame
patient = tk.Frame


note.add(timer , text='timer')
note.patient(timer , text='timer')


############################## timer########################
p1=tk.StringVar()
p1.set('patient1')
tk.Label(root,textvariable=p1, (row=0, column=0))
p2=tk.StringVar()
p2.set('patient2')
tk.Label(root,textvariable=p2).grid(row=0, column=0))
p1=tk.StringVar()
p1.set('patient3')
tk.Label(root,textvariable='p3',(row=0, column=0))

#tk.Label(root,textvariable='', (row=0, column=1))

#tk.Label(root,textvariable='', (row=0, column=1))






tk.Button(root,text='')
grid(row=2, column=0)

tk.Button(root,text='')
grid(row=2, column=0)

tk.Button(root,text='')
grid(row=2, column=0)

tk.Button(root,text='')
grid(row=2, column=0)











root.mainlop()