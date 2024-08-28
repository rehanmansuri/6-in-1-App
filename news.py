from pygooglenews import GoogleNews
import tkinter as tk
from PIL import ImageTk, Image
def news():
    top = tk.Toplevel()
    top.geometry('1280x720+100-100')
    top.config(bg='#4D4D4D')
    top_img = Image.open('news.png')
    top_img = ImageTk.PhotoImage(top_img)
    top.iconphoto(False, top_img)






    head = tk.Label(top, text='Headlines', font=('Algerian', 30), foreground='yellow', background='#4D4D4D',
                    highlightthickness=0)
    head.grid(row=0, column=0, sticky='w', padx=8)

    lb = tk.Listbox(top, height=41, width=212, background='#4D4D4D', highlightthickness=0, foreground='aqua',
                    font=('Times Roman', 15))
    lb.grid(row=1, column=0, padx=8, )

    gn = GoogleNews(lang='en', country='IN')

    news = gn.top_news()
    i = 0
    for item in news['entries']:
        t = item['title']
        i = i + 1
        t = str(i) + '. ' + t
        lb.insert('end', t)
        lb.insert('end', '')

        if i == 15:
            break

    top.mainloop()