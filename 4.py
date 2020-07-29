import tkinter as tk


def stop():
    pass


root = tk.Tk()
timer={'left':1200,
       'right':1200}

tk.Label(root,
         text='left player',
         font=("times", 20, "italic")) \
    .grid(row=0, column=0)
tk.Label(root,
         text='right player',
         font=("times", 20, "italic")) \
    .grid(row=0, column=1)



l_timer = tk.StringVar()
l_timer.set('20:00')
tk.Label(root,
         textvariable=l_timer,
         font=("times", 20, "italic")) \
    .grid(row=1, column=0)


r_timer = tk.StringVar()
r_timer.set('20:00')
tk.Label(root,
         textvariable=r_timer,
         font=("times", 20, "italic")) \
    .grid(row=1, column=1)
tk.Button(root,
          text="stop",
          command=stop,
          font=('courier', 20)) \
    .grid(row=2, column=0)

tk.Button(root
          , text="stop"
          , command=stop
          , font=("courier", 20)) \
    .grid(row=2, column=1)
tk.Button(root,
          text="start",
          command=stop,
          font=('courier', 30)) \
    .grid(row=3, column=0, columnspan=2)

tk.Button(root
          , text="cancel"
          , command=root.destroy
          , font=("courier", 30)) \
    .grid(row=4, column=0, columnspan=2)



root.mainloop()