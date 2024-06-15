from tkinter import *
import tkinter.messagebox

def after_page1():
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
    #else:
        #cardetails()
    

window =Tk()
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
#label4 = Label(window, text='Come on, Now let\'s get started with your booking!!' ,bg="green" ,fg="black", font="Times 20 bold", justify="center").place(x=350,y=220)


#start/drop location

label6=Label(window, text='Select pick-up and drop location in Bangalore:',font='Times 16',bg='teal').place(x=50,y=290)
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
