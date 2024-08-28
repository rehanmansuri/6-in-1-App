import tkinter as tk
import PyDictionary as pd
from PIL import ImageTk, Image


def dic():
    def click():



        print('line 12', text_v)
        word = text_v.get()

        print(word)

        translated = pd.PyDictionary.meaning(word)
        translated = str(translated)
        length = len(translated)
        i = 0
        a = ''
        b = ''
        list_trans = translated.split()
        num_words = len(list_trans)
        lines = num_words//15
        lines = lines+1
        for j in range(0, lines):
            q = 15*(j+1)
            temp = " ".join(list_trans[j*15:q])
            a = a+'\n'
            a = a+temp



        print(a)






        meaning.config(text=a)


    win = tk.Toplevel()
    win.title('Dictionary')
    win.geometry('1280x720+100-100')
    win.config(background='#4D4D4D')
    win_img = Image.open('dictionary.png')
    win_img = ImageTk.PhotoImage(win_img)
    win.iconphoto(False, win_img)

    text_v = tk.StringVar(master=win)

    canvas = tk.Canvas(win)
    canvas.config(highlightthickness=0, width=1280, background='#4D4D4D')
    canvas.pack()



    m_canvas = tk.Canvas(win)
    m_canvas.config(height=720, width=1110, highlightthickness=0, background='#4D4D4D')

    m_canvas.pack()

    meaning = tk.Label(m_canvas, text='', font=('Comic Sans MS', 15), justify='left', background='#4D4D4D',
                       foreground='yellow')
    meaning.grid(row=1, column=0)

    m_label = tk.Label(m_canvas, text='Meaning', font=('Comic Sans MS', 30), background='#4D4D4D', foreground='aqua')
    m_label.grid(row=0, column=0)
    print('line 31', text_v)


    head = tk.Label(canvas, text='Dictionary:', font=('Comic Sans MS', 30), background='#4D4D4D', foreground='aqua')
    head.pack()
    lab = tk.Label(canvas, text='Enter a word', font=('Comic Sans MS', 30), background='#4D4D4D', foreground='aqua')
    lab.pack()

    inp = tk.Entry(canvas, textvariable=text_v)

    inp.pack()
    lab2 = tk.Label(canvas, text='', background='#4D4D4D')
    lab2.pack()
    btn = tk.Button(canvas, text='Submit', command=click)
    btn.pack()

    win.mainloop()
