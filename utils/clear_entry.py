from tkinter import *

class ClearEntry():
    def __init__(self, obj):
        self.obj = obj

    # clear all the entry after complete the task
    def clear(self):
        self.obj.entry1.delete(0, END)
        self.obj.entry2.delete(0, END)
        self.obj.entry3.delete(0, END)
        self.obj.entry4.delete(0, END)
        self.obj.entry5.delete(0, END)
        self.obj.entry6.delete(0, END)
        self.obj.entry7.delete(0, END)
        self.obj.entry8.delete(0, END)
        self.obj.entry9.delete(0, END)
        self.obj.entry10.delete(0, END)
        self.obj.entry11.delete(0, END)
        self.obj.entry12.delete(0, END)
        self.obj.entry13.delete(0, END)
        self.obj.entry14.delete(0, END)
        self.obj.entry15.delete(0, END)
        self.obj.entry16.delete(0, END)
        self.obj.entry17.delete(0, END)
