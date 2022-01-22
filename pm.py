from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import MySQLdb as mdb
DBNAME="sql4466852"
DBHOST="sql4.freemysqlhosting.net"
DBPASS="dmG4WzJZLG"
DBUSER="sql4466852"

root=Tk()
root.geometry('400x400')
root.title("Solomonr Abo Bilal")
root.resizable(0,0)
Label(root , text = "Full name : " , font = "arial 10 bold ").grid(column=0 ,row =0 ,padx=10,pady=10,sticky="w")
Label(root , text = "E_mail or phone : " , font = "arial 10 bold ").grid(column=0 ,row =1 ,padx=10,pady=10,sticky="w")
Label(root , text = "password : " , font = "arial 10 bold ").grid(column=0 ,row =2 ,padx=10,pady=10,sticky="w")
Label(root , text = "password again  : " , font = "arial 10 bold ").grid(column=0 ,row =3 ,padx=10,pady=10,sticky="w")

name=ttk.Entry(root , width=20, font="arial 15 bold")
name.grid(column=1 , row=0 , padx=10 , pady=20)

email=ttk.Entry(root , width=20, font="arial 15 bold")
email.grid(column=1 , row=1 , padx=10 , pady=20)

pass1=ttk.Entry(root , width=20, font="arial 15 bold" , show="*")
pass1.grid(column=1 , row=2 , padx=10 , pady=20)

pass2=ttk.Entry(root , width=20, font="arial 15 bold" ,show="*")
pass2.grid(column=1 , row=3 , padx=10 , pady=20)

btn=ttk.Button(root , text="create account" , command= lambda:save_info(name.get(),email.get(),pass1.get(),pass2.get()))
btn.grid(column=0 , row=4 ,padx=10 , pady=10 ,columnspan=2 ,ipadx=50 , ipady=4)
def save_info(name , email , ps1 , ps2):
    if ps1 == ps2:
        password=ps1
        db=mdb.connect(DBHOST , DBUSER , DBPASS , DBNAME)
        cur=db.cursor()
        print("connected")

        insert="INSERT INTO table_db (name, email ,password) VALUES (%s ,%s ,%s)"
        values=(name , email ,password)
        try:
            cur.execute(insert, values)
            db.commit()
        except Exception as e :
            print("Was a error "+e)
        db.close()
        msg.showinfo("Data save sucssefull" ,"Data Saved ")
    else:
        msg.showerror("Error password ","password is incorect")

root.mainloop()
