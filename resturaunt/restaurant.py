import tkinter as tk
import tkinter.ttk as ttk



labek_cnf={"bg":"91ff35"}
Label_cnf={"bg":"#f50057"}


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$ food information $$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
i ={
     "1" : {"name": 'ye chiz bahal',
            'rating':5 ,
            "review": 47,
            "price":1.5},
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
tk.Label(f1 , text= rating ,cnf=Label_cnf) .grid(row= 1 , column=0)

price =str(i['1']['price']) + "$"
tk.Label(f1 , text= price , cnf=Label_cnf).grid(row= 2 , column=0)




root.mainloop()