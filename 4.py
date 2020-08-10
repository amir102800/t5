import tkinter as tk
from threading import Thread
from time import sleep


def stop(side):
    global flag
    if side == 'left':
        flag = True
    else:
        flag = False


def start(t):
    while True:
        sleep(1)
        if flag:
            timer["right"] -= 1
            m, s = divmod(timer['right'], 60)

            r_timer.set('%02d:%02d' % (m, s))

        else:
            timer["left"] -= 1
            m, s = divmod(timer['left'], 60)

            l_timer.set('%02d:%02d' % (m, s))


root = tk.Tk()

timer = {'left': 1200,
         'right': 1200}
flag = False
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
          command=lambda: stop('left'),
          font=('courier', 20)) \
    .grid(row=2, column=0)

tk.Button(root
          , text="stop"
          , command=lambda: stop('right')
          , font=("courier", 20)) \
    .grid(row=2, column=1)

tk.Button(root
          , text="cancel"
          , command=root.destroy
          , font=("courier", 30)) \
    .grid(row=4, column=0, columnspan=2)

thread = Thread(target=start, args=(0,))
thread.start()

root.mainloop()
