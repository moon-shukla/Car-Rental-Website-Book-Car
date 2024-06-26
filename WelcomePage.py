# welcome page
from tkinter import *
import tkinter.messagebox

def after_proceed():
    action_ans=StringVar(page0)
    action_ans=action.get()
    if action_ans=='Select':
        tkinter.messagebox.showinfo('Error', 'Please select an action to proceed.')
    elif action_ans=='Book a Car':
        pass
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
        select_car_model_part2()
    elif selected_car_category=='SEDAN':
        car_nameoptions=["Maruti Swift Dzire", "Hyundai Verna", "Honda City",  "Tata Tigor", "Maruti Ciaz"]
        select_car_model_part2()
    elif selected_car_category=='HATCHBACK':
        car_nameoptions=["Tata Altroz", "Maruti Swift", "Hyundai Grand i10",  "Tata Tiago", "Maruti Celerio"]
        select_car_model_part2()
    

def select_car_model_part2():
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
        print(return_list)
    
    
    
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
