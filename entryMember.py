from tkinter import *
from PIL import Image,ImageTk
import webbrowser
import datetime
import pyttsx3
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
def insert():
    i=idvalue.get()
    name=Namevalue.get()
    in_out=var.get()
    timedate=Time_Datevalue.get()

    con = mysql.connect(host="localhost", user="root", password="", database="AMS")
    cursor = con.cursor()
    cursor.execute("select * from addmember where id='" + idvalue.get() + "'")
    result = cursor.fetchall()

    # id2 = -1
    temp = 0
    for rows in result:
        # id1 = rows[0]
        temp = 1
        if temp == 1:
            if i == "" or name == "" or in_out == "" or timedate == "":
                engine = pyttsx3.init()
                """ RATE"""
                voices = engine.getProperty('voices')
                rate = engine.getProperty('rate')  # getting details of current speaking rate
                # print (rate)                        #printing current voice rate
                engine.setProperty('rate', 150)  # setting up new voice rate

                """VOLUME"""
                engine.setProperty('voice', voices[1].id)
                volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
                # print (volume)                          #printing current volume level
                engine.setProperty('volume', 1.0)
                engine.say("All fields are required")
                # messagebox.sho winfo("Hello baba",)

                engine.runAndWait()

                messagebox.showinfo("insert", "All field are required")

            else:
                con=mysql.connect(host="localhost",user="root",password="",database="AMS")
                cursor=con.cursor()
                cursor.execute("insert into memberentry values('"+i+"','"+name+"','"+in_out+"','"+timedate+"')")
                cursor.execute("commit");
                engine = pyttsx3.init()
                """ RATE"""
                voices = engine.getProperty('voices')
                rate = engine.getProperty('rate')  # getting details of current speaking rate
                # print (rate)                        #printing current voice rate
                engine.setProperty('rate', 150)  # setting up new voice rate

                """VOLUME"""
                engine.setProperty('voice', voices[1].id)
                volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
                # print (volume)                          #printing current volume level
                engine.setProperty('volume', 1.0)
                engine.say("insert Successfully")
                # messagebox.showinfo("Hello baba",)

                engine.runAndWait()
                messagebox.showinfo("insert","insert Successfully")
                con.close()
                idvalue.set("")
                Namevalue.set("")
        elif temp!=1:

            messagebox.showinfo("Delete Status", "invalid")


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


st=Label(ban,text="MEMBERS ENTRY",font=("bold",30),fg="black",bg="#FAE5D3").place(x=400,y=50)
Id=Label(ban,text="ID",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=150)
Name=Label(ban,text="Name",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=190)
In_Out=Label(ban,text="In/Out",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=230)
Time_Date=Label(ban,text="Time/Date",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=270)

idvalue=StringVar()
Namevalue=StringVar()
var = StringVar(root)
var.set("in")
Time_Datevalue=StringVar()

IdEntry=Entry(ban,textvariable=idvalue,width=50,borderwidth=2, relief="solid",).place(x=440,y=150)
NameEntry=Entry(ban,textvariable=Namevalue, width=50,borderwidth=2, relief="solid").place(x=440,y=190)
In_OutEntry = OptionMenu(root, var, "in", "out").place(x=620,y=270)
# In_OutEntry=Entry(ban, width=50,borderwidth=2, relief="solid").place(x=440,y=230)
TimeDateEntry=Entry(ban,textvariable=Time_Datevalue, width=50,borderwidth=2, relief="solid")
TimeDateEntry.insert(0, time.asctime())
TimeDateEntry.place(x=440,y=270)

b=Button(root, text='Submit', width=13, bg='brown', fg='white',command=insert).place(x=720, y=350)
root.mainloop()