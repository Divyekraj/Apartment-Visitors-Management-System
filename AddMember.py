from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as messagebox
import mysql.connector as mysql
import pyttsx3
import webbrowser
root=Tk()
root.geometry("1920x1080")
root.title("Add Members")
def s():
    # i=idvalue.get()
    con = mysql.connect(host="localhost", user="root", password="", database="AMS")
    cursor = con.cursor()
    cursor.execute("select MAX(id) from addmember")
    result = cursor.fetchall()
    id1 = 0
    id2 = -1
    temp = 0
    # ans=1
    for rows in result:
        id1 = rows[0]
        # if id1=="":
        #     c="1";
        #     idvalue.set(c)
        ans=id1+1
    idvalue.set(ans)
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
    name=Namevalue.get();
    email=Emailvalue.get();
    mobile=Mobilevalue.get();
    floorno=FloorNovalue.get();
    platno=PlatNovalue.get();
    parkingno=ParkingNovalue.get();

    if i=="" or name=="" or email=="" or mobile=="" or floorno=="" or platno=="" or parkingno=="":

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
        messagebox.showinfo("insert", "All field are required")

    else:
        con=mysql.connect(host="localhost",user="root",password="",database="AMS")
        cursor=con.cursor()
        cursor.execute("insert into addmember values('"+i+"','"+name+"','"+email+"','"+mobile+"','"+floorno+"','"+platno+"','"+parkingno+"')")
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
        engine.say("Record Insert Successfully")
        # messagebox.showinfo("Hello baba",)

        engine.runAndWait()
        # messagebox.showinfo("insert", "Record Insert Successfully")
        messagebox.showinfo("insert","insert Successfully")
        con.close()
        idvalue.set("")
        Namevalue.set("");
        Emailvalue.set("");
        Mobilevalue.set("");
        FloorNovalue.set("");
        PlatNovalue.set("");
        ParkingNovalue.set("");



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

st=Label(ban,text="ADD MEMBERS",font=("bold",30),fg="black",bg="#FAE5D3").place(x=400,y=50)
Id=Label(ban,text="ID",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=150)
Name=Label(ban,text="Name",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=190)
Email=Label(ban,text="Email",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=230)
Mobile=Label(ban,text="Mobile",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=270)
FloorNo=Label(ban,text="FloorNo",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=310)
PlatNo=Label(ban,text="PlatNo",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=350)
ParkingNo=Label(ban,text="ParkingNo",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=390)

idvalue=StringVar()
Namevalue=StringVar()
Emailvalue=StringVar()
Mobilevalue=StringVar()
FloorNovalue=StringVar()
PlatNovalue=StringVar()
ParkingNovalue=StringVar()

IdEntry=Entry(ban,textvariable=idvalue, width=50,borderwidth=2, relief="solid").place(x=440,y=150)
NameEntry=Entry(ban,textvariable=Namevalue, width=50,borderwidth=2, relief="solid").place(x=440,y=190)
EmailEntry=Entry(ban,textvariable=Emailvalue, width=50,borderwidth=2, relief="solid").place(x=440,y=230)
MobileEntry=Entry(ban,textvariable=Mobilevalue, width=50,borderwidth=2, relief="solid").place(x=440,y=270)
FloorNoEntry=Entry(ban,textvariable=FloorNovalue, width=50,borderwidth=2, relief="solid").place(x=440,y=310)
PlatNoEntry=Entry(ban,textvariable=PlatNovalue, width=50,borderwidth=2, relief="solid").place(x=440,y=350)
ParkingNoEntry=Entry(ban,textvariable=ParkingNovalue, width=50,borderwidth=2, relief="solid").place(x=440,y=390)

getid=Button(root, text='Get ID', width=5, bg='brown', fg='white',command=s).place(x=930, y=194)
b=Button(root, text='Submit', width=13, bg='brown', fg='white',command=insert).place(x=700, y=480)
root.mainloop()