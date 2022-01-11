#import the required libraries
from tkinter import *
from tkinter import filedialog
import win32api
import os

#Create an instance of tkinter frame or window
win= Tk()

win.title('Print Hard Copy')
win.geometry("700x400")

#Define function
def print_file():
   path = filedialog.askopenfilename()
   if path:
      os.startfile(path, "print")

#Create a button for printing event
button= Button(win, text="Choose a File to Print", command=print_file).pack(pady= 20)

#Keep running the window or frame
win.mainloop()