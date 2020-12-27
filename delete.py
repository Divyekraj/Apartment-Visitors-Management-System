from tkinter import *
from PIL import Image,ImageTk
import webbrowser
import datetime
import time
import tkinter.messagebox as messagebox
import mysql.connector as mysql

root=Tk()
root.geometry("1920x1080")
root.title("Members Entry")
def h():
    webbrowser.open_new("home.py")
    root.destroy()
def d1():
    webbrowser.open_new("dashboard.py")
    root.destroy()
def d2():
    webbrowser.open_new("memberview.py")
    root.destroy()
def d3():
    webbrowser.open_new("AddMember.py")
    root.destroy()
def d4():
    webbrowser.open_new("entryMember.py")
    root.destroy()
def d5():
    webbrowser.open_new("visiter.py")
    root.destroy()
def d6():
    webbrowser.open_new("login.py")

    root.destroy()
def delete():
    # i=idvalue.get()
    con = mysql.connect(host="localhost", user="root", password="", database="AMS")
    cursor = con.cursor()
    cursor.execute("select * from addmember where id='"+idvalue.get()+"'")
    result = cursor.fetchall()
    id1=0
    id2=-1
    temp=0
    for rows in result:
        # id1 = rows[0]
        temp=1
    if temp==1:
            con = mysql.connect(host="localhost", user="root", password="", database="AMS")
            cursor = con.cursor()
            cursor.execute("delete from addmember where id='" + idvalue.get() + "'")
            cursor.execute("commit");
            messagebox.showinfo("Delete Status", "Delete Successfully")
            con.close()
            # continue
    else:

             messagebox.showinfo("Delete Status", "invalid")

    # "all done"

f2=Frame(root, bg="red",borderwidth=2,relief="solid")
f2.pack(side="top",fill="x")
l=Label(f2,text="Khandesh Apartment Pune",bg="red",font=("bold",20))
l.pack()
f1=Frame(root, bg="#FAD7A0",borderwidth=4,relief="solid")
f1.pack(side="left",fill="y")
# l=Label(f1,text="Dashboard",bg="white")
Home=Button(f1,text="Home",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20),command=h)
Home.pack(padx=10,pady=25)
Dashboard=Button(f1,text="Dashboard",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20),command=d1)
Dashboard.pack(padx=10,pady=25)
Members=Button(f1,text="Members",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20),command=d2)
Members.pack(padx=10,pady=25)
Addmember=Button(f1,text="Add Member",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20),command=d3)
Addmember.pack(padx=10,pady=25)
MemberEntry=Button(f1,text="Member Entry",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20),command=d4)
MemberEntry.pack(padx=10,pady=25)
visiter=Button(f1,text="Visiter",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20),command=d5)
visiter.pack(padx=10,pady=25)
logout=Button(f1,text="Logout",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20),command=d6)
logout.pack(padx=10,pady=25)
ban=Frame(root, bg="#FAE5D3",borderwidth=4,relief="solid",width=1920,height=500)
ban.pack(side="left",fill="y")


st=Label(ban,text="Delete Members",font=("bold",30),fg="black",bg="#FAE5D3").place(x=400,y=50)
Id=Label(ban,text="ID",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=400,y=150)

idvalue=StringVar()

IdEntry=Entry(ban,textvariable=idvalue,width=50,borderwidth=2, relief="solid",).place(x=440,y=150)
b=Button(root, text='Delete', width=13, bg='brown', fg='white',command=delete).place(x=720, y=250)
root.mainloop()