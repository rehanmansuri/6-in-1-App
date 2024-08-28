import tkinter as tk
from PIL import ImageTk, Image
import dictionary as dc
import text_editor as te
import to_do_list as tdl
import news
import digi_calendar as dica
import Calculator as clc

win = tk.Tk()
win.geometry("1280x720+100-100")
win.config(bg='#4D4D4D')

win.title('Main Menu')
title_image = Image.open('splash.jpg')
title_image = ImageTk.PhotoImage(title_image)
win.iconphoto(False, title_image)


calc_icon = Image.open("calculator_icon.png")
calc_icon = ImageTk.PhotoImage(calc_icon)
print(type(calc_icon))
calc_button = tk.Button(win, image=calc_icon, borderwidth=0, bg='#4D4D4D', highlightthickness=0, activebackground='#4D4D4D', command=clc.calc)
calc_button.place(x=310, y=180, anchor='center')

timetable_icon = Image.open("timetable_icon.png")
timetable_icon = ImageTk.PhotoImage(timetable_icon)
timetable_button = tk.Button(win, image=timetable_icon, borderwidth=0, command=dica.dates_, bg='#4D4D4D', highlightthickness=0, activebackground='#4D4D4D')
timetable_button.place(x=630, y=180, anchor='center')

texteditor_icon = Image.open("texteditor_icon.png")
texteditor_icon = ImageTk.PhotoImage(texteditor_icon)
texteditor_button = tk.Button(win, image=texteditor_icon, borderwidth=0, command=te.text_editor, bg='#4D4D4D', highlightthickness=0, activebackground='#4D4D4D')
texteditor_button.place(x=950, y=180, anchor='center')

dictionary_icon = Image.open("dictionary.png")
dictionary_icon = ImageTk.PhotoImage(dictionary_icon)
dictionary_button = tk.Button(win, image=dictionary_icon, borderwidth=0, command=dc.dic, bg='#4D4D4D', highlightthickness=0, activebackground='#4D4D4D')
dictionary_button.place(x=630, y=450, anchor='center')

todo_icon = Image.open("todo.png")
todo_icon = ImageTk.PhotoImage(todo_icon)
todo_button = tk.Button(win, image=todo_icon, borderwidth=0, command=tdl.tdl, bg='#4D4D4D', highlightthickness=0, activebackground='#4D4D4D')
todo_button.place(x=310, y=450, anchor='center')

news_icon = Image.open("news.png")
news_icon = ImageTk.PhotoImage(news_icon)
news_button = tk.Button(win, image=news_icon, borderwidth=0, command=news.news, bg='#4D4D4D', highlightthickness=0, activebackground='#4D4D4D')
news_button.place(x=950, y=450, anchor='center')

win.mainloop()
