import tkinter as tk
import tkinter.ttk as ttk 


def start():
    pass


root = tk.Tk()


note = ttk.Notebook()
note.grid(row=0 , column=0)

timer = tk.Frame()
patient = tk.Frame()


note.add(timer , text='timer')
note.add(patient , text='patient')


############################## timer########################
p1=tk.StringVar()
p1.set('patient1')
tk.Label(timer,textvariable=p1).grid (row=0, column=0)
p2=tk.StringVar()
p2.set('patient2')
tk.Label(timer,textvariable=p2).grid(row=0, column=1)
p3=tk.StringVar()
p3.set('patient3')
tk.Label(timer,textvariable=p3).grid(row=0, column=2)

t1 = tk.StringVar()
t1.set('00:00')
tk.Label(timer,textvariable=t1).grid (row=1, column=0)

t2 = tk.StringVar()
t2.set('00:00')
tk.Label(timer,textvariable=t2).grid (row=1, column=1)

t3 = tk.StringVar()
t3.set('00:00')
tk.Label(timer,textvariable=t3).grid (row=1, column=2)
#############################timer third row button#####################################################
tk.Button(timer,text='start' , command=start).grid(row=2, column=0)
tk.Button(timer,text='start',command=start ).grid(row=2, column=1)
tk.Button(timer,text='start',command=start).grid(row=2, column=2)
###################################timer last row cancel################################################
tk.Button(timer,text='cancel' ,command=root.destroy).grid(row=3 , column=0, columnspan =3)
########################################################################################################
patient1 =tk.LabelFrame(patient)


root.mainloop()