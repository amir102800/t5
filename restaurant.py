import tkinter as tk
import tkinter.ttk as ttk



labek_cnf={"bg":"91ff35"}
Label_cnf={"bg":"#f50057"}

root = tk.Tk()





note = ttk.Notebook()
note.grid(row=0, column=0)
drink = tk.Frame()
food = tk.Frame()
reciept=tk.Frame()
note.add(drink, text='drink')
note.add(food, text='food')
note.add(reciept, text='reciept')



#########################################################
f1 = tk.Frame(food)
f1.grid(row=1, column=0  )

#d1 = tk.Frame(drink)
#d1.grid(row=0 , coulmn=0 )

##r1 = tk.Frame(reciept)
##r1.grid(row=0 , coulmn=0 )

tk.Label(f1 , text = "chiken with rice",cnf=Label_cnf) .grid(row=0, column=0)
tk.Label(f1 , text= "⍟⍟⍟⍟⍟" ,cnf=Label_cnf) .grid(row= 1 , column=0)
tk.Label(f1 , text= "1.5$" , cnf=Label_cnf).grid(row= 2, column=0)

root.mainloop()