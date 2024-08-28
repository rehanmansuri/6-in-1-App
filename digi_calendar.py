import tkinter as tk
import tkcalendar as tkc
import datetime as dt
from PIL import ImageTk, Image
import babel.numbers
def dates_():
    top = tk.Toplevel()
    top.geometry('1280x720+100-100')
    top.title("Calendar")
    top.config(bg='#4D4D4D')
    top_img = Image.open('timetable_icon.png')
    top_img = ImageTk.PhotoImage(top_img)
    top.iconphoto(False, top_img)






    year = dt.date.today().year

    month = dt.date.today().month

    day = dt.date.today().day

    print(year, month, day)

    cal = tkc.Calendar(top, year=year, month=month, day=day, selectmode='none')
    cal.pack(fill='both', expand=True, pady=40, padx=40)

    top.mainloop()