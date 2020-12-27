from tkinter import *
from PIL import Image,ImageTk
import webbrowser
import datetime
import time
import tkinter.messagebox as messagebox
import mysql.connector as mysql
def s():
    # i=idvalue.get()
    con = mysql.connect(host="localhost", user="root", password="", database="AMS")
    cursor = con.cursor()
    cursor.execute("select MAX(id) from addmember")
    result = cursor.fetchall()
    id1 = 0
    id2 = -1
    temp = 0
    for rows in result:
        id1 = rows[0]
        ans=id1+1
    idvalue.set(ans)

root=Tk()
root.geometry("400x400")

idvalue=StringVar()

IdEntry=Entry(root,textvariable=idvalue,width=50,borderwidth=2, relief="solid").pack()

b=Button(root, text='Submit', width=13, bg='brown', fg='white',command=s).pack()
root.mainloop()