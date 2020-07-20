import tkinter as tk




root = tk.Tk()

a1=tk.Label(root,text='' , bg= 'yellow' , font=('times', 20))
a1.grid(row=0,column=0 ,rowspan=3, sticky=tk.S+tk.N)

a2=tk.Label(root,text='' , bg= 'red' , font=('times', 20))
a2.grid(row=0,column=1, columnspan=3, sticky=tk.W+tk.E)

a3=tk.Label(root,text='' , bg= 'green' , font=('times', 20))
a3.grid(row=1,column=1,rowspan=2 ,sticky=tk.S+tk.N)

a4=tk.Label(root,text='' , bg= 'blue' , font=('times', 20))
a4.grid(row=1,column=2 ,rowspan=2 ,sticky=tk.N+tk.S )

a5=tk.Label(root,text='' , bg= 'pink' , font=('times', 20))
a5.grid(row=1,column=3)

a6=tk.Label(root,text='L6' , bg= 'yellow' , font=('times', 20))
a6.grid(row=2,column=3)


root.mainloop()