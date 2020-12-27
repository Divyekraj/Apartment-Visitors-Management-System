from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as messagebox
import webbrowser
root=Tk()
root.geometry("1920x1080")
root.title("Login Page")
def dis():
    a=idvalue.get()
    b=Namevalue.get()
    if (a == "div" and b == "123"):
        webbrowser.open_new("home.py")
        root.destroy()


    else:
        messagebox.showinfo("insert", "Wrong Id or Password")

def h():

    webbrowser.open_new("home.py")
    root.destroy()
def d6():
    webbrowser.open_new("login.py")
    root.destroy()

f2=Frame(root, bg="#D35400",borderwidth=2,relief="solid")
f2.pack(side="top",fill="x")
l=Label(f2,text="Khandesh Apartment Pune",bg="#D35400",font=("bold",20))
l.pack()
f1=Frame(root, bg="#FAD7A0",borderwidth=4,relief="solid")
f1.pack(side="left",fill="y")
# l=Label(f1,text="Dashboard",bg="white")
Home=Button(f1,text="Home",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20),command=h)
Home.config(state = DISABLED)
Home.pack(padx=10,pady=25)
Dashboard=Button(f1,text="Dashboard",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20))
Dashboard.config(state = DISABLED)
Dashboard.pack(padx=10,pady=25)
Members=Button(f1,text="Members",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20))
Members.config(state = DISABLED)
Members.pack(padx=10,pady=25)
Addmember=Button(f1,text="Add Member",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20))
Addmember.config(state = DISABLED)
Addmember.pack(padx=10,pady=25)
MemberEntry=Button(f1,text="Member Entry",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20))
MemberEntry.config(state = DISABLED)
MemberEntry.pack(padx=10,pady=25)
visiter=Button(f1,text="Visiter",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20))
visiter.config(state = DISABLED)
visiter.pack(padx=10,pady=25)

logout=Button(f1,text="Login",bg="white",fg="Blue",borderwidth=2,relief="solid",font=(20),command=d6)
logout.pack(padx=10,pady=25)
ban=Frame(root, bg="#FAE5D3",borderwidth=4,relief="solid",width=1920,height=500)
ban.pack(side="left",fill="y")

st=Label(ban,text="Login Page",font=("bold",30),fg="black",bg="#FAE5D3").place(x=470,y=50)
Id=Label(ban,text="UserID",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=150)
Name=Label(ban,text="Password",font=("Arial Bold",12),fg="black",bg="#FAE5D3").place(x=300,y=190)

idvalue=StringVar()
Namevalue=StringVar()
IdEntry=Entry(ban,textvariable=idvalue, width=50,borderwidth=2, relief="solid").place(x=440,y=150)
NameEntry=Entry(ban,show="*",textvariable=Namevalue, width=50,borderwidth=2, relief="solid").place(x=440,y=190)

# getid=Button(root, text='Get ID', width=5, bg='brown', fg='white').place(x=930, y=194)
b=Button(root, text='Login', width=13, bg='brown', fg='white',command=dis).place(x=700, y=280)

root.mainloop()