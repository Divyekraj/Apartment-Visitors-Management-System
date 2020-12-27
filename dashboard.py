from tkinter import *
from PIL import Image,ImageTk
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
def d9():
    webbrowser.open_new("delete.py")
    root.destroy()
def d10():
    webbrowser.open_new("update.py")
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
ban=Frame(root, bg="#FAE5D3",borderwidth=4,relief="solid")
ban.pack(side="left",fill="y")
# ban.config(state='disabled')
b=Button(root, text='Members Entry list', width=40, bg='brown', fg='white',command=d7).place(x=300, y=100)

b2=Button(root, text='Visitors Entry list', width=40, bg='brown', fg='white',command=d8).place(x=800, y=100)

b3=Button(root, text='Delete', width=40, bg='brown', fg='white',command=d9).place(x=300, y=400)

b4=Button(root, text='Update', width=40, bg='brown', fg='white',command=d10).place(x=800, y=400)
# l=Label(f1,text="Members",bg="white")
# l.pack()

root.mainloop()