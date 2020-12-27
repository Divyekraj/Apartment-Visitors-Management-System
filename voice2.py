
import pyttsx3
import tkinter.messagebox as messagebox
engine = pyttsx3.init()
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
engine.setProperty('rate', 100)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)
engine.say("Enter any number")
# messagebox.showinfo("Hello baba",)

engine.runAndWait()