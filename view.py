import tkinter as tk

def change(event):
    print('Hi')
    if ceil_11['text'] != 'X':
        ceil_11['text'] = 'X'
    else:
        print('It done yet')

win = tk.Tk()
win.geometry('312x306+100+200')
win.title('Крестики - нолики')

ceil_11 = tk.Label(win, text = "A", font = "Arial 32", width = 4, height = 2)
ceil_12 = tk.Label(win, text = "A", font = "Arial 32", width = 4, height = 2)
ceil_13 = tk.Label(win, text = "A", font = "Arial 32", width = 4, height = 2)
ceil_21 = tk.Label(win, text = "B", font = "Arial 32", width = 4, height = 2)
ceil_22 = tk.Label(win, text = "B", font = "Arial 32", width = 4, height = 2)
ceil_23 = tk.Label(win, text = "B", font = "Arial 32", width = 4, height = 2)
ceil_31 = tk.Label(win, text = "C", font = "Arial 32", width = 4, height = 2)
ceil_32 = tk.Label(win, text = "C", font = "Arial 32", width = 4, height = 2)
ceil_33 = tk.Label(win, text = "C", font = "Arial 32", width = 4, height = 2)

ceil_11.config(bd = 1, bg = '#ffaaaa', relief = "solid")
ceil_12.config(bd = 1, bg = '#ffaaaa', relief = "solid")
ceil_13.config(bd = 1, bg = '#ffaaaa', relief = "solid") 
ceil_21.config(bd = 1, bg = '#ffaaaa', relief = "solid") 
ceil_22.config(bd = 1, bg = '#ffaaaa', relief = "solid") 
ceil_23.config(bd = 1, bg = '#ffaaaa', relief = "solid")
ceil_31.config(bd = 1, bg = '#ffaaaa', relief = "solid")
ceil_32.config(bd = 1, bg = '#ffaaaa', relief = "solid")
ceil_33.config(bd = 1, bg = '#ffaaaa', relief = "solid")

ceil_11.bind('<Button-1>', change)
ceil_12.bind('<Button-1>', change)
ceil_13.bind('<Button-1>', change)
ceil_21.bind('<Button-1>', change)

ceil_11.grid(row = 0, column = 0)
ceil_12.grid(row = 0, column = 1)
ceil_13.grid(row = 0, column = 2)
ceil_21.grid(row = 1, column = 0)
ceil_22.grid(row = 1, column = 1)
ceil_23.grid(row = 1, column = 2)
ceil_31.grid(row = 2, column = 0)
ceil_32.grid(row = 2, column = 1)
ceil_33.grid(row = 2, column = 2)

win.mainloop()
