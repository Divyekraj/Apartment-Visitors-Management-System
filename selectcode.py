from tkinter import *
import pymysql
connection = pymysql.connect(host="localhost", user="root", passwd="", database="demo")
cursor = connection.cursor()

#
data = cursor.execute("SELECT * from emp")

master = Tk()
master.geometry('500x500')
master.title('CLUBS')
Label1 = Label(master, text="ID", width=10)
Label1.grid(row=0, column=0)
Label2 = Label(master, text="NAME", width=10)
Label2.grid(row=0, column=1)
Label3 = Label(master, text="track", width=10)
Label3.grid(row=0, column=2)

rows = cursor.fetchall()
for index,dat in enumerate(data):
# for index, dat in enumerate(data):
    Label(master, text=dat[0]).grid(row=index + 1, column=0)
    Label(master, text=dat[1]).grid(row=index + 1, column=1)
    Label(master, text=dat[2]).grid(row=index + 1, column=2)
connection.commit()
connection.close()
self.tex.config(state=tk.DISABLED)