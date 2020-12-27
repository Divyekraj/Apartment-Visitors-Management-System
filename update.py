from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as messagebox
import mysql.connector as mysql
import webbrowser
root=Tk()
root.geometry("1920x1080")
root.title("Add Members")
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
def search():
    i = idvalue.get()
    if i == "":
        messagebox.showinfo("insert", "ID field are required")
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
        con = mysql.connect(host="localhost", user="root", password="", database="AMS")
        cursor = con.cursor()
        cursor.execute("select * from addmember where id='" + i + "'")
        result = cursor.fetchall()
        for rows in result:
            id1 = rows[0]
            Name1 = rows[1]
            Email1 = rows[2]
            Mobile1 = rows[3]
            FloorNo1 = rows[4]
            PlatNo1 = rows[5]
            ParkingNo1 = rows[6]


    else:

        messagebox.showinfo("Delete Status", "invalid")

    idvalue.set(i)

    Namevalue.set(Name1)

    Emailvalue.set(Email1)

    Mobilevalue.set(Mobile1)

    FloorNovalue.set(FloorNo1)

    PlatNovalue.set(PlatNo1)

    ParkingNovalue.set(ParkingNo1)

    con.close()  # continue
def update():
    i=idvalue.get()
    name=Namevalue.get();
    email=Emailvalue.get();
    mobile=Mobilevalue.get();
    floorno=FloorNovalue.get();
    platno=PlatNovalue.get();
    parkingno=ParkingNovalue.get();
    if i=="" or name=="" or email=="" or mobile=="" or floorno=="" or platno=="" or parkingno=="":
        messagebox.showinfo("insert","All field are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="AMS")
        cursor=con.cursor()
        cursor.execute("update addmember set id='"+i+"', name='"+name+"',email='"+email+"',mobile='"+mobile+"',floorno='"+floorno+"',platno='"+platno+"',parkingno='"+parkingno+"' where id='"+i+"'")
        cursor.execute("commit");
        messagebox.showinfo("Update","Update Successfully")
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

b=Button(root, text='Update', width=13, bg='brown', fg='white',command=update).place(x=800, y=480)
b1=Button(root, text='Search', width=13, bg='brown', fg='white',command=search).place(x=650, y=480)
root.mainloop()