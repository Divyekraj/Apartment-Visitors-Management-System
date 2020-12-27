from tkinter import *
import webbrowser
def dis():
    a=idEntry.get()
    b=pasEntry.get()
    if(a=="" or b==""):
        messagebox.showinfo("insert", "All field are required")
    if(a=="div" and b=="123"):
        print("yes")
        webbrowser.open_new("home.py")


    else:
        print("no")

root = Tk()
root.geometry('1920x1080')
root.title("Registration Form")


Lform = Label(root, text="Login form", width=20, font=("bold", 20))
Lform.place(x=90, y=53)

id = Label(root, text="ID", width=20, font=("bold", 10))
id.place(x=80, y=130)

idEntry = Entry(root,width=28,borderwidth=2, relief="solid")
# idEntry.insert(0,"hello")
idEntry.place(x=190, y=130)

pas = Label(root, text="Password", width=20, font=("bold", 10))
pas.place(x=68, y=180)

pasEntry = Entry(root,width=28,borderwidth=2, relief="solid")
pasEntry.place(x=190, y=180)

Button(root, text='Submit', width=10, bg='brown', fg='white',command=dis).place(x=190, y=220)

root.mainloop()
