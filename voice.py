import pyttsx3
import tkinter.messagebox as messagebox
def a(messag):
    engine=pyttsx3.init()
    engine.say('{}'.format(messag ))
    engine.runAndWait()

messag='''hello baba'''
messagebox.showinfo(a(messag),"Hello baba")
