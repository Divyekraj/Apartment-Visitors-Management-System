from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as messagebox
import mysql.connector as mysql
from tkinter import ttk
import webbrowser
root=Tk()
root.geometry("1920x1080")

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
def d7():
    webbrowser.open_new("memberentrylist.py")
    root.destroy()
def d8():
    webbrowser.open_new("visiterentrylist.py")
    root.destroy()

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
# ban.config(state='disabled')
con = mysql.connect(host="localhost", user="root", password="", database="AMS")
cursor = con.cursor()
cursor.execute("select * from visiter")
# cursor.execute("commit");
rows=cursor.fetchall()

ban=Frame(root, bg="#FAE5D3",borderwidth=4,relief="solid",width=800,height=500)
ban.pack(side="left",fill="y",anchor='center')

tv=ttk.Treeview(ban,columns=(1,2,3,4,5,6,7,8),show="headings",height = 33, selectmode = "extended")
# tv=ttk.Treeview(ban)
tv["columns"]=("1","2","3","4","5","6","7","8")
tv.column("1", width=130,anchor='center')
tv.column("2", width=130,anchor='center')
tv.column("3", width=130,anchor='center')
tv.column("4", width=130,anchor='center')
tv.column("5", width=130,anchor='center')
tv.column("6", width=130,anchor='center')
tv.column("7", width=150,anchor='center')
tv.column("8", width=150,anchor='center')

tv.heading(1,text="Name")
tv.heading(2, text="Mobile")
tv.heading(3, text="Flatno")
tv.heading(4, text="Floorno")
tv.heading(5, text="Whom_To_Meet")
tv.heading(6, text="Reason_To_Meet")
tv.heading(7, text="Entry_time")
tv.heading(8, text="Entry_time")

for i in rows:
    tv.insert('','end',values=i)
tv.pack()
con.close()
# l=Label(f1,text="Members",bg="white")
# l.pack()

root.mainloop()