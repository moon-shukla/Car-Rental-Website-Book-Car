from tkinter import *
import tkinter.messagebox

#python-mysql interface
import mysql.connector as mc
global mycon
mycon=mc.connect(host="localhost", user="root", passwd="tiger", database="project")
global mycursor
mycursor=mycon.cursor(buffered=True)

def userdetails():
    root.destroy()
    global master
    master=Tk()
    master.title("User Details")
    master.geometry("600x600")
    master.configure(bg="grey")

    #labels
    UserDetails=Label(master, text="User Details",bg="black", fg="white", font="Times 20 bold", justify="center").place(x=210, y=10)
    label2=Label(master, text="Name:", bg="teal", fg="black", font="Times 16").place(x=40, y=70)
    label3=Label(master, text="Age:", bg="teal", fg="black", font="Times 16").place(x=40, y=110)
    label4=Label(master, text="Address:", bg="teal", fg="black", font="Times 16").place(x=40, y=150)
    label5=Label(master, text="Ph. No:", bg="teal", fg='black', font='Times 16').place(x=40, y=190)
    label6=Label(master, text="Aadhar No:", bg="teal", fg='black', font='Times 16').place(x=40, y=230)
    label7=Label(master, text="Email ID:", bg="teal", fg='black', font="Times 16").place(x=40, y=270)
    label8=Label(master, text="Security Deposit: Rs 3000", bg="green", fg="white", font="Times 16").place(x=40, y=330)
    label9=Label(master, text="Select payment method:", bg="teal", fg="black", font="Times 16").place(x=40, y=370)

    #entry fields
    global Name
    Name=Entry(master, fg="black", font="Times 16", cursor="xterm")
    Name.place(x= 150, y=70)

    global Age
    Age=Entry(master, fg="black", font="Times 16", cursor='xterm')
    Age.place(x=150, y=110)
    
    global Address
    Address=Entry(master, fg="black", font="Times 16", cursor="xterm")
    Address.place(x=150, y=150)

    global PhNo
    PhNo=Entry(master, fg='black', font="Times 16", cursor="xterm")
    PhNo.place(x=150, y=190)

    global Aadhar
    Aadhar=Entry(master, fg='black', font="Times 16", cursor="xterm")
    Aadhar.place(x=150, y=230)
    
    global Email
    Email=Entry(master, fg='black', font="Times 16", cursor="xterm")
    Email.place(x=150, y=270)

    #drop down list
    global payment_method
    payment_method=StringVar(master)
    options=["Credit Card", "Debit Card", "UPI"]
    payment_method.set(options[0])
    droplist=OptionMenu(master, payment_method, *options)
    droplist.config(width=10, font="Times 16")
    droplist.place(x=290, y=365)
    
    #pay button
    paybutton=Button(master, text="Confirm Booking", bg="darkblue", fg="white", font="Times 14", height=1, width=20, command=finalmsg)
    paybutton.place(x=170, y=430)

    master.mainloop()

def finalmsg():
    global payment_method_ans
    payment_method_ans=StringVar(master)
    payment_method_ans=payment_method.get()
    li=[]
    li.append(Name.get())
    li.append(Age.get())
    li.append(Address.get())
    li.append(PhNo.get())
    li.append(Aadhar.get())
    li.append(Email.get())
    li.append(payment_method_ans)
    if '' not in li:
        sql_userdata(li) #calling sql_userdata function to insert user data in the sql table
        tkinter.messagebox.showinfo("Important", "Note: The actual rental amount must be paid at the time the car is dropped off.\n Thank you for choosing Rent-A-Car :)\n")
        master.destroy()
    else:
        tkinter.messagebox.showinfo("Error","Please fill all the details to complete the booking process.")

def sql_userdata(li):
    query_='Insert into userdata(name, age, address, phno, aadhar, email, payment_method) values(%s, %s, %s, %s, %s, %s, %s)'
    val=(li)
    mycursor.execute(query_,val)
    mycon.commit()
    li2=[Aadhar.get(),a]
    query__='Update cardata set aadhar=%s where carname=%s'
    mycursor.execute(query__,li2)
    mycon.commit()
    query___='Update cardata set pickup_drop_location=%s, pickup_date=%s, pickup_time=%s, drop_date=%s, drop_time=%s where aadhar=%s'
    page1_li.append(Aadhar.get())
    mycursor.execute(query___, page1_li)
    mycon.commit()
    
    print('Booking Successful!')

def select_car_model_part1():
    global car_name
    car_name=StringVar(root)
    car_name.set('Select')
    selected_car_category=car_category.get()
    if selected_car_category=='Select':
        tkinter.messagebox.showinfo('Error', 'Please select car type.')
    else:
        car_list.append(selected_car_category)
        global car_nameoptions
        if selected_car_category=='SUV':
            car_nameoptions=["Mahindra Thar", "Toyota Fortuner", "Tata Harrier",  "Hyundai Creta", "Mahindra Scorpio"]
            select_car_model_part2()
        elif selected_car_category=='SEDAN':
            car_nameoptions=["Maruti Swift Dzire", "Hyundai Verna", "Honda City",  "Tata Tigor", "Maruti Ciaz"]
            select_car_model_part2()
        elif selected_car_category=='HATCHBACK':
            car_nameoptions=["Tata Altroz", "Maruti Swift", "Hyundai Grand i10",  "Tata Tiago", "Maruti Celerio"]
            select_car_model_part2()

def select_car_model_part2():
    carnames_droplist=OptionMenu(root, car_name, *car_nameoptions)
    carnames_droplist.config(width=12, font="Times 16")
    carnames_droplist.place(x=330,y=400)

def after_page2():
    global a
    a=car_name.get()
    if a=='Select':
        tkinter.messagebox.showinfo('Error', 'Please select car model.')
    else:
        car_list.append(a)
        car_tuple=tuple(car_list)
        query="select * from cardata"
        mycursor.execute(query)
        records=mycursor.fetchall()
        if len(records)==0:
            query1="Insert into cardata(carcategory,carname) values(%s,%s)"
            mycursor.execute(query1,car_tuple)
            mycon.commit()
            userdetails()
        else:
            for row in records:
                if a in row:
                    tkinter.messagebox.showinfo("Car Unavailable", "Sorry! This car is already booked. Please select another car.")
                else:
                    continue
                
            else:
                count=0
                for row in records:
                    if a not in row:
                        count+=1
                if count==len(records):
                    if len(car_tuple)>2:
                        car=car_list[-1]
                    elif len(car_tuple)==2:
                        car=a
                    car_list1=(d[car],car)
                    car_tuple1=tuple(car_list1)
                    query1="Insert into cardata(carcategory,carname) values(%s,%s)"
                    mycursor.execute(query1,car_tuple1)
                    mycon.commit()
                    userdetails()
                

global car_list
car_list=[]

global d
d={"Mahindra Thar":"SUV", "Toyota Fortuner":"SUV", "Tata Harrier":"SUV",  "Hyundai Creta":"SUV", "Mahindra Scorpio":"SUV",
   "Maruti Swift Dzire":"SEDAN", "Hyundai Verna":"SEDAN", "Honda City":"SEDAN",  "Tata Tigor":"SEDAN", "Maruti Ciaz":"SEDAN",
   "Tata Altroz":"HATCHBACK", "Maruti Swift":"HATCHBACK", "Hyundai Grand i10":"HATCHBACK",  "Tata Tiago":"HATCHBACK",
   "Maruti Celerio":"HATCHBACK"}
   

#root
def cardetails():
    window.destroy()
    global root
    root = Tk()
    root.title("Car Details")
    root.geometry("600x600")
    root.configure(bg="grey")

    #Labels
    ct0 = Label(root, text="Pricing Details", bg="black", fg="white", font="Times 20 bold", justify="center").place(x=210, y=10)
    ct1 = Label(root, text = "SUV:", bg="green", fg="white", font="Times 16").place(x=160, y=70)
    ct2 = Label(root, text = "SEDAN:", bg="green", fg="white", font="Times 16").place(x=160, y=110)
    ct3 = Label(root, text = "HATCHBACK:", bg="green", fg="white", font="Times 16").place(x=160, y=150)

    #pphr = price per hour
    pphr1=Label(root, text = "600 INR/hour",font="Jersey 18").place(x=330, y=67)
    pphr2=Label(root, text = "500 INR/hour",font="Jersey 18").place(x=330, y=107)
    pphr3=Label(root, text = "400 INR/hour",font="Jersey 18").place(x=330, y=147)
    selectcartype = Label(root, text = "Select Car type: ", bg="teal", fg="black", font="Times 18").place(x=150, y=220)

    #droplist 1
    global car_category
    car_category=StringVar(root)
    car_options=["SUV", "SEDAN", "HATCHBACK"]
    car_category.set('Select')
    cartypes_droplist=OptionMenu(root, car_category, *car_options)
    cartypes_droplist.config(width=12, font="Times 16")
    cartypes_droplist.place(x=330, y=220)
    global selected_car_category
    selected_car_category=StringVar(root)
    selected_car_category.set('')

    #button 1
    selectcarbtn1= Button(root, text="Select Car Model", bg="black", fg="white", font="Times 16", command=select_car_model_part1)
    selectcarbtn1.place(x=230, y=320)

    car_model = Label(root, text = "Car Model:", bg="teal", fg="black", font="Times 16").place(x=150, y=400)

    #button 2
    nextbtn= Button(root, text="    Next    ", bg="black", fg="white", font="Times 16", command=after_page2)
    nextbtn.place(x=250, y=490)

    root.mainloop()

#page 1
def after_page1():
    global page1_li
    page1_li=[]

    location=StringVar(window)
    location.set('')
    location=pickup.get()

    pickup_month=StringVar(window)
    pickup_month.set('')
    pickup_month=clicked.get()

    pickup_date=StringVar(window)
    pickup_date.set('')
    pickup_date=clicked2.get()

    pickup_hour=StringVar(window)
    pickup_hour.set('')
    pickup_hour=clicked3.get()

    pickup_min=StringVar(window)
    pickup_min.set('')
    pickup_min=clicked4.get()

    drop_month=StringVar(window)
    drop_month.set('')
    drop_month=clicked5.get()

    drop_date=StringVar(window)
    drop_date.set('')
    drop_date=clicked6.get()

    drop_hour=StringVar(window)
    drop_hour.set('')
    drop_hour=clicked7.get()

    drop_min=StringVar(window)
    drop_min.set('')
    drop_min=clicked8.get()

    page1_li.append(location)
    page1_li.append(pickup_month+' '+pickup_date)
    page1_li.append(pickup_hour+':'+pickup_min)
    page1_li.append(drop_month+' '+drop_date)
    page1_li.append(drop_hour+':'+drop_min)

    if 'Select' in page1_li:
        tkinter.messagebox.showinfo('Error','Please select the pickup and drop location.')
    elif (pickup_hour=='Hours' or drop_hour=='Hours') :
        tkinter.messagebox.showinfo('Error','Please select the time.')
    elif (pickup_min=='Mins' or drop_min=='Mins') :
        tkinter.messagebox.showinfo('Error','Please select the time.')
    else:
        cardetails()
    
def page1():
    page0.destroy()
    global window
    window=Tk()
    window.title("Rent-A-Car")
    window.geometry("1000x1000")
    window.configure(bg="grey")

    #intro
    label = Label(window, text='Welcome to Rent-A-Car!!! \n There\'s one for all!' ,bg="black", fg='white', font="Times 20 bold", justify="center")
    label.place(x=310, y=10)
    label1 = Label(window, text='We bring to you the best with a very\nsimplified process.' ,bg="black", fg='white', font="Times 18", justify="center")
    label1.place(x=295,y=90)

    Adv ='''The Rent-A-Car Advantage:'''
    adv='''>> Fuel cost included >> No hidden charges >> Go anywhere (ALL INDIA PERMIT)\n >> Damage Insurance >> 24X7 Roadside assistance '''

    label2= Label(window, text=Adv,bg="brown" ,fg="white", font="Times 18 bold ", justify="center").place(x=330,y=170)
    label3=Label(window, text=adv ,bg="lightgrey" ,fg="black", font="Times 16 ",justify='center').place(x=130,y=220)
    
    #start/drop location
    label6=Label(window, text='Select pick-up and drop location in Bengaluru:',font='Times 16',bg='teal').place(x=50,y=290)
    global pickup
    pickup=StringVar(window)
    pickup_and_drop_locations=['Hebbal','Jayanagar','JP Nagar','Kormanagala','Whitefield','KR Puram', 'Yelahanka New Town',
                               'Rajajinagar']
    pickup.set('Select')
    pickupdroplist=OptionMenu(window, pickup,*pickup_and_drop_locations)
    pickupdroplist.config(width=10, font='Times 16')
    pickupdroplist.place(x=450, y=285)

    label5= Label(window, text='Pickup:' ,bg="green" ,fg="black", font="Times 16 bold").place(x=50 ,y=330)

    #pick date
    label7=Label(window, text='Month and Date:',font='Times 16',bg='teal').place(x=50,y=370)
    global clicked
    clicked=StringVar()
    clicked.set("Jan")
    options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31]
    global clicked2
    clicked2=StringVar()
    clicked2.set(options[0])
    drop=OptionMenu(window,clicked, "Jan","Feb","Mar","Apr","May","June","Jul","Aug","Sept","Oct","Nov","Dec")
    drop.config(width=6, font='Times 16')
    drop2=OptionMenu(window,clicked2,*options)
    drop2.config(width=2, font='Times 16')
    drop2.place(x=340,y=365)
    drop.place(x=210,y=365)

    #pick time,(formality)
    label7=Label(window, text='Time:',font='Times 16',bg='teal').place(x=50,y=420)

    optionsh=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    optionsm=['00','05','10','15','20','25','30','35','40','45','50','55']
    global clicked3
    clicked3=StringVar()
    clicked3.set('Hours')
    global clicked4
    clicked4=StringVar()
    clicked4.set('Mins')

    drop3=OptionMenu(window,clicked3,*optionsh)
    drop4=OptionMenu(window,clicked4,*optionsm)
    drop3.config(width=4, font='Times 16')
    drop4.config(width=4, font='Times 16')

    drop3.place(x=120,y=415)
    drop4.place(x=220,y=415)

    label5= Label(window, text='Drop:' ,bg="green" ,fg="black", font="Times 16 bold").place(x=50,y=460)

    #drop date
    label8=Label(window, text='Month and Date:',font='Times 16',bg='teal').place(x=50,y=500)
    global clicked5
    clicked5=StringVar()
    clicked5.set("Jan")
    options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31]
    global clicked6
    clicked6=StringVar()
    clicked6.set(options[0])

    drop5=OptionMenu(window,clicked5, "Jan","Feb","Mar","Apr","May","June","Jul","Aug","Sept","Oct","Nov","Dec")
    drop5.config(width=6, font='Times 16')
    drop6=OptionMenu(window,clicked6,*options)
    drop6.config(width=2, font='Times 16')
    drop6.place(x=340,y=495)
    drop5.place(x=210,y=495)

    #drop time,(formality)
    label9=Label(window, text='Time:',font='Times 16',bg='teal').place(x=50,y=550)
    optionshr=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23',]
    optionsmn=['00','05','10','15','20','25','30','35','40','45','50','55']
    global clicked7
    clicked7=StringVar()
    clicked7.set('Hours')
    global clicked8
    clicked8=StringVar()
    clicked8.set('Mins')

    drop7=OptionMenu(window,clicked7,*optionshr)
    drop7.config(width=4, font='Times 16')
    drop8=OptionMenu(window,clicked8,*optionsmn)
    drop8.config(width=4, font='Times 16')
    drop7.place(x=120,y=545)
    drop8.place(x=220,y=545)

    btn=Button (window,text='Next', justify=CENTER,bg='black',fg='white',font='Times 16', height=2, width=6, command=after_page1).place(x=450,y=600) 

    window.mainloop()

#page 0
def after_proceed():
    action_ans=StringVar(page0)
    action_ans=action.get()
    if action_ans=='Select':
        tkinter.messagebox.showinfo('Error', 'Please select an action to proceed.')
    elif action_ans=='Book a Car':
        page1()
    elif action_ans=='Return the Car':
        #labels
        label3=Label(page0, text='Authentication:', bg='green', fg='black', font='Times 18')
        label3.place(x=220, y=250)
        label4=Label(page0, text='Select Car Category:', bg='teal', fg='black', font='Times 16')
        label4.place(x=70, y=310)
        
        #car category dropdown
        global car_category
        car_category=StringVar(page0)
        car_options=["SUV", "SEDAN", "HATCHBACK"]
        car_category.set('Select')
        cartypes_droplist=OptionMenu(page0, car_category, *car_options)
        cartypes_droplist.config(width=12, font="Times 16")
        cartypes_droplist.place(x=255, y=305)
        global selected_car_category
        selected_car_category=StringVar(page0)
        selected_car_category.set('')

        #button
        button2=Button(page0, text='Next', bg='black', fg='white', font='Times 16', command=after_proceed_2)
        button2.place(x=450, y=305)
        
def after_proceed_2():
    global car_name
    car_name=StringVar(page0)
    car_name.set('Select')
    selected_car_category=car_category.get()
    global car_nameoptions
    if selected_car_category=="Select":
        tkinter.messagebox.showinfo('Error','Please select car category.')
    elif selected_car_category=='SUV':
        car_nameoptions=["Mahindra Thar", "Toyota Fortuner", "Tata Harrier",  "Hyundai Creta", "Mahindra Scorpio"]
        select_car_model()
    elif selected_car_category=='SEDAN':
        car_nameoptions=["Maruti Swift Dzire", "Hyundai Verna", "Honda City",  "Tata Tigor", "Maruti Ciaz"]
        select_car_model()
    elif selected_car_category=='HATCHBACK':
        car_nameoptions=["Tata Altroz", "Maruti Swift", "Hyundai Grand i10",  "Tata Tiago", "Maruti Celerio"]
        select_car_model()
    

def select_car_model():
    label5=Label(page0, text='Select Car Model:', bg='teal', fg='black', font='Times 16')
    label5.place(x=70, y=370)
    carnames_droplist=OptionMenu(page0, car_name, *car_nameoptions)
    carnames_droplist.config(width=12, font="Times 16")
    carnames_droplist.place(x=255,y=365)
    label6=Label(page0, text="Aadhar No:", bg="teal", fg='black', font='Times 16')
    label6.place(x=70, y=420)
    global aadhar_entry
    aadhar_entry=Entry(page0, font='Times 16', cursor='xterm', fg='black')
    aadhar_entry.place(x=255, y=420)

    #button3
    button3=Button(page0, text="Return", bg='black', fg='white', font='times 16', command=after_return)
    button3.place(x=250, y=480)

def after_return():
    car_name_ans=StringVar(page0)
    car_name_ans=car_name.get()
    if car_name_ans=='Select':
        tkinter.messagebox.showinfo('Error','Please select car name.')
    elif aadhar_entry.get()=='':
        tkinter.messagebox.showinfo('Error','Please enter Aadhar No.')
    else:
        return_list=[]
        return_list.append(car_name_ans)
        return_list.append(aadhar_entry.get())
        return_tuple=tuple(return_list)
        query='Select * from cardata where (carname=%s and aadhar=%s)'
        mycursor.execute(query,return_tuple)
        records=mycursor.fetchall()
        if len(records)==0:
            tkinter.messagebox.showinfo('Error', 'Authentication failed.\nPlease enter correct details.')
        else:
            query2='delete from cardata where (carname=%s and aadhar=%s)'
            mycursor.execute(query2, return_list)
            mycon.commit()
            query3='delete from userdata where aadhar=%s'
            aadhar_list=[]
            aadhar_list.append(aadhar_entry.get())
            mycursor.execute(query3,aadhar_list)
            mycon.commit()
            tkinter.messagebox.showinfo('Confirmation', 'Return Successful!\nThank you for choosing Rent-A-Car')
            print('Return Successful!')

            page0.destroy()

global page0
page0=Tk()
page0.geometry('600x600')
page0.configure(bg='grey')
page0.title('Action')

#labels
label1=Label(page0, text='Rent - A - Car', bg='black', fg='white', font='Times 20 bold')
label1.place(x=210, y=15)
label2=Label(page0, text='Select Action:', bg='teal', fg='black', font='times 16')
label2.place(x=150, y=110)

#button 1
button1=Button(page0, text='Proceed', bg='black', fg='white', font='Times 16', command=after_proceed)
button1.place(x=250, y=190)

#action drop list
global action
action=StringVar(page0)
action.set('Select')
action_options=['Book a Car', 'Return the Car']
action_droplist=OptionMenu(page0, action, *action_options)
action_droplist.config(width=12, font='Times 16')
action_droplist.place(x=300, y=105)

page0.mainloop()

