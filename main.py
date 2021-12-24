
from tkinter import Tk, Button, Scale, Canvas, Label, StringVar, Entry, Toplevel, messagebox
from tkinter.colorchooser import askcolor
from PIL import Image
import os

class FileNamePopup:
    def __init__(self, master):
        top = self.top = Toplevel(master)
        self.lbl = Label(top, text="Choose a file name:")
        self.lbl.pack()
        self.ent_filename = Entry(top)
        self.ent_filename.pack()
        self.btn_ok = Button(top, text="Ok", command=self.cleanup)
        self.btn_ok.pack()


    def cleanup(self):
        self.filename = self.ent_filename.get()
        self.top.destroy()



