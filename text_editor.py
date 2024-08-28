import tkinter
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def text_editor():
    def quitApp():
        root.destroy()

    def cut():
        TextArea.event_generate(("<>"))

    def copy():
        TextArea.event_generate(("<>"))

    def paste():
        TextArea.event_generate(("<>"))

    def about():
        showinfo("Notepad", "Notepad by Code With Harry")

    # Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")

    root.geometry("644x788")

    # Add TextArea
    TextArea = Text(root, font="lucida 13")

    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()

