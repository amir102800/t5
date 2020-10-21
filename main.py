import tkinter as tk
import tkinter.ttk as ttk


root=tk.Tk
root.title("bank")


#top= tk.TopLevel()
#top.title(form)
note = ttk.Notebook()


regiester = tk.Frame



login_form = tk.Frame()


note.add(regiester_form , text='regiester')
note.add(login_form , text='login')

note.grid(row=0 column=)

tk.Label(regiester_form ,text='username:').grid(row=0 , column=0)
tk.Label(regiester_form ,text='Password:').grid(row=1 , column=0)

form_user = tk.stringVar()
form_pass = tk.stringVar()
tk.entery(register_form ,textvarieble=form_user)




root.mainloop()