#python-sql connection
import mysql.connector as mc
mycon=mc.connect(host="localhost", user="root", passwd="tiger", database="project")
mycursor=mycon.cursor()

#tkinter
from tkinter import *
import tkinter.messagebox
def message():
    tkinter.messagebox.showinfo("Important", "Note: The actual rental amount must be paid at the time the car is dropped off.\n Thank you for choosing Rent-A-Car :)\n")
    li=[]
    li.append(Name.get())
    li.append(Age.get())
    li.append(Address.get())
    li.append(PhNo.get())
    li.append(Email.get())
    sql_userdata(li)
def sql_userdata(li):
    query='Insert into userdata(name, age, address, phno, email) values(%s, %s, %s, %s, %s)'
    val=(li)
    mycursor.execute(query,val)
    mycon.commit()
    print(mycursor.rowcount, 'record inserted')
#root
root=Tk()
root.title("Rent-A-Car")
root.geometry("600x600")
root.configure(bg="grey")

#labels
UserDetails=Label(root, text="User Details",bg="black", fg="white", font="Times 20 bold", justify="center").place(x=210, y=10)
label2=Label(root, text="Name:", bg="grey", fg="black", font="Times 16").place(x=40, y=70)
label3=Label(root, text="Age:", bg="grey", fg="black", font="Times 16").place(x=40, y=110)
label4=Label(root, text="Address:", bg="grey", fg="black", font="Times 16").place(x=40, y=150)
label5=Label(root, text="Ph. No:", bg="grey", fg='black', font='Times 16').place(x=40, y=190)
label6=Label(root, text="Aadhar No:", bg="grey", fg='black', font='Times 16').place(x=40, y=230)
label7=Label(root, text="Email ID:", bg="grey", fg='black', font="Times 16").place(x=40, y=270)
label8=Label(root, text="Security Deposit: Rs 3000", bg="green", fg="white", font="Times 16").place(x=40, y=330)
label9=Label(root, text="Select payment method:", bg="grey", fg="black", font="Times 16").place(x=40, y=370)

#entry fields
Name=Entry(root, fg="black", font="Times 16", cursor="xterm")
Name.place(x= 150, y=70)

Age=Entry(root, fg="black", font="Times 16", cursor='xterm')
Age.place(x=150, y=110)

Address=Entry(root, fg="black", font="Times 16", cursor="xterm")
Address.place(x=150, y=150)

PhNo=Entry(root, fg='black', font="Times 16", cursor="xterm")
PhNo.place(x=150, y=190)

Aadhar=Entry(root, fg='black', font="Times 16", cursor="xterm")
Aadhar.place(x=150, y=230)

Email=Entry(root, fg='black', font="Times 16", cursor="xterm")
Email.place(x=150, y=270)

#getting values from entry widget

li=[]
li.append(Name.get())
li.append(Age.get())
li.append(Address.get())
li.append(PhNo.get())
li.append(Email.get())


#drop down list
variable=StringVar(root)
options=["Credit Card", "Debit Card", "UPI"]
variable.set(options[0])
droplist=OptionMenu(root, variable, *options)
droplist.config(width=10, font="Times 16")
droplist.place(x=290, y=365)

#pay button
paybutton=Button(root, text="Confirm Booking", bg="darkblue", fg="white", font="Times 14", height=1, width=20, command=message).place(x=170, y=430)

root.mainloop()

