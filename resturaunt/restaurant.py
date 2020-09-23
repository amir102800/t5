import tkinter as tk
import tkinter.ttk as ttk
from tkinter  import Image,PhotoImage



Label_cnf={"bg":"#f50057"}


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$ food information $$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
i ={
     "1" : {"name": 'humburger',
            'rating':5 ,
            "review": 47,
            "price":1.5,
            "img": "howcuttingdo.gif"},
}

###############################################################################




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
name = i['1']['name']
tk.Label(f1 , text = name,cnf=Label_cnf) .grid(row=0, column=0)

rating =  i['1']['rating'] * '★'+'('+str(i['1']['review']) + ')'
tk.Label(f1 , text= rating ,cnflLabel_cnf) .grid(row= 1 , column=1)

price =str(i['1']['price']) + "$"
tk.Label(f1 , text= price , cnf=Label_cnf).grid(row= 0 . column=1)

des =str(i['1']['desciription']) + "$"
tk.Label(f1 , text= price , cnf=Label_cnf).grid(row= 0 , column=1)

img =PhotoImage(file=i['1']['img']).subsample(4)
tk.Label(f1 , image= img , borderwidth=12 , relief='solid') .grid(row=0  , column=2 , rowspan=4)


root.mainloop()