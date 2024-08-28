import numpy
import pandas as pd
import tkinter as tk
import datetime as dt
import os
from PIL import ImageTk,Image
list_items = pd.DataFrame(columns=['Task'])
def tdl():
    global list_items
    top = tk.Toplevel()
    top.geometry("1280x720+100-100")
    top.title('To do list')
    top.config(bg='#4D4D4D')
    top_img = Image.open('todo.png')
    top_img = ImageTk.PhotoImage(top_img)
    top.iconphoto(False, top_img)





    canvas = tk.Frame(top, highlightthickness=0, height=100, width=1000, bg='#4D4D4D')
    canvas.grid_propagate(False)
    canvas.grid(column=0, row=0)
    lb = tk.Listbox(top, width=91, height=24, font=('Times Roman', 15))
    lb.grid(row=1, column=0, sticky='w')
    new_item = tk.StringVar(master=top)





    def adding():


        new_item2 = new_item.get()
        print(new_item2)

        add.delete(0, 'end')


        data_to_be_added = [new_item2]
        list_items.loc[len(list_items.index)] = data_to_be_added

        print(list_items.columns[0])
        lb.insert('end', data_to_be_added)

    def saving():

        if os.path.isfile('./list.csv'):
            os.remove('list.csv')

        save_file = list_items
        save_file.loc[len(save_file.index)] = x
        save_file.to_csv('list.csv', index=False)
        top.destroy()
    def opening():
        global list_items

        open_file = pd.read_csv('list.csv')

        print(open_file)

        a = len(open_file.index)-1
        print(a)
        new_var = open_file._get_value(a, col='Task')
        print(new_var)
        if new_var == x:

            open_file = open_file.drop(labels=a, axis=0)
            #print('type of open file is ', type(open_file.iat[1,0]), open_file.iat[1, 0])
            list_items = list_items.append(open_file)
            #print('type of list_items is   ', type(open_file.iat[1, 0]), open_file.iat[1, 0])

            for i in range(0, a):
                g = list_items._get_value(i, col='Task')
                print(g, type(g))
                if isinstance(g, numpy.ndarray):
                    g = g[0]
                    lb.insert('end', g)
                else:
                    lb.insert('end', g)

        else:
            tk.Message(top, text='The data you are trying to load was not saved today.\n'
                                 ' Only the data that was saved today could be loaded.')
    x = dt.datetime.now()
    d = x.strftime('%d')
    m = x.strftime('%b')
    y = x.strftime('%Y')
    x = d + ' ' + m + ' ' + y
    print(x)

    date = tk.Label(canvas, text=x, font=('Comic Sans MS', 20), bg='#4D4D4D', fg='aqua')
    date.grid(row=0, column=0)

    to_do = tk.Label(canvas, text='                  To Do List', font=('Comic Sans MS', 20), bg='#4D4D4D', fg='aqua')
    to_do.grid(row=0, column=2)

    spaces = tk.Label(canvas, text='                 ', bg='#4D4D4D', fg='aqua')
    spaces.grid(row=0, column=3)

    add_item = tk.Label(canvas, text='Add a task ', font=('Comic Sans MS', 20), bg='#4D4D4D', fg='aqua')
    add_item.grid(row=0, column=4)

    add = tk.Entry(canvas, textvariable=new_item, width=30)
    add.grid(row=0, column=5)

    spaces2 = tk.Label(canvas, text='       ', bg='#4D4D4D', fg='aqua')
    spaces2.grid(row=0, column=6)

    add_bt = tk.Button(canvas, text='Add', width=6, command=adding)
    add_bt.grid(row=0, column=7)



    checks = tk.Label(canvas, text=' ', bg='#4D4D4D', fg='aqua')
    checks.grid(row=1, column=0)
    tasks = tk.Label(canvas, text='Tasks ', font=('Comic Sans MS', 20), bg='#4D4D4D', fg='aqua')
    tasks.grid(row=1, column=0)

    save_bt = tk.Button(canvas, command=saving, text='Save', font=('Times Roman', 15))
    save_bt.grid(row=1, column=1)

    load_bt = tk.Button(canvas, text='Open', font=('Comic Sans MS', 15), command=opening)
    load_bt.grid(row=1, column=2)


    vertical_sb = tk.Scrollbar(top, orient='vertical', background='grey', activebackground='grey')
    vertical_sb.grid(row=1, column=1, sticky='ns')
    lb.config(yscrollcommand=vertical_sb.set)
    vertical_sb.config(command=lb.yview)

    top.mainloop()
