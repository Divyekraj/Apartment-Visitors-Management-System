from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as messagebox
import mysql.connector as mysql
import webbrowser
import pyttsx3
import datetime
import time

root=Tk()
root.geometry("1920x1080")
root.title("Add Visitor")
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
    name=Namevalue.get();
    mobile=Mobilevalue.get();
    platno = PlatNovalue.get();
    floorno=FloorNovalue.get();
    Whom_To_Meet=Whom_To_MeetValue.get();
    Reason_To_Meet=Reason_To_Meetvalue.get();
    Entry_Time=Entry_Timevalue.get();
    Exit_Time=Exit_Timevalue.get();
    if name=="" or mobile=="" or floorno=="" or platno=="" or Whom_To_Meet=="" or Reason_To_Meet=="" or Entry_Time== "" or Exit_Time=="":
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
        # messagebox.showinfo("Hello baba",)

        engine.runAndWait()
        messagebox.showinfo("insert","All field are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="AMS")
        cursor=con.cursor()
        cursor.execute("insert into visiter values('"+name+"','"+mobile+"','"+platno+"','"+floorno+"','"+Whom_To_Meet+"','"+Reason_To_Meet+"','"+Entry_Time+"','"+Exit_Time+"')")
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
        Namevalue.set("");
        Mobilevalue.set("");
        FloorNovalue.set("");
        PlatNovalue.set("");
        Whom_To_MeetValue.set("");
        Reason_To_Meetvalue.set("");

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
st=Label(ban,text="ADD VISITORS",font=("bold",30),fg="black",bg="#FAE5D3").place(x=400,y=50)
Name=Label(ban,text="Name",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=150)
Mobile=Label(ban,text="Mobile",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=190)
FlatNo=Label(ban,text="FlatNo",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=230)
FloorNo=Label(ban,text="FloorNo",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=270)
Whom_To_Meet=Label(ban,text="Whom To Meet",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=310)
Reason_To_Meet=Label(ban,text="Reason To Meet",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=350)
Entry_Time=Label(ban,text="Entry_Time",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=390)
Exit_Time=Label(ban,text="Exit_Time",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=430)

Namevalue=StringVar()
Mobilevalue=StringVar()
PlatNovalue=StringVar()
FloorNovalue=StringVar()
Whom_To_MeetValue=StringVar()
Reason_To_Meetvalue=StringVar()
Entry_Timevalue=StringVar()
Exit_Timevalue=StringVar()


NameEntry=Entry(ban,textvariable=Namevalue, width=50,borderwidth=2, relief="solid").place(x=440,y=150)
MobileEntry=Entry(ban,textvariable=Mobilevalue, width=50,borderwidth=2, relief="solid").place(x=440,y=190)
FlatEntry=Entry(ban,textvariable=PlatNovalue, width=50,borderwidth=2, relief="solid").place(x=440,y=230)
FloorNoEntry=Entry(ban,textvariable=FloorNovalue, width=50,borderwidth=2, relief="solid").place(x=440,y=270)
Whom_To_MeetEntry=Entry(ban,textvariable=Whom_To_MeetValue, width=50,borderwidth=2, relief="solid").place(x=440,y=310)
Reason_To_MeetEntry=Entry(ban,textvariable=Reason_To_Meetvalue, width=50,borderwidth=2, relief="solid").place(x=440,y=350)
Entry_TimeEntry=Entry(ban,textvariable=Entry_Timevalue, width=50,borderwidth=2, relief="solid")
Entry_TimeEntry.insert(0, time.asctime())
Entry_TimeEntry.place(x=440,y=390)

Exit_TimeEntry=Entry(ban,textvariable=Exit_Timevalue, width=50,borderwidth=2, relief="solid")
Exit_TimeEntry.insert(0, time.asctime())
Exit_TimeEntry.place(x=440,y=430)

b=Button(root, text='Submit', width=13, bg='brown', fg='white',command=insert).place(x=700, y=550)
root.mainloop()