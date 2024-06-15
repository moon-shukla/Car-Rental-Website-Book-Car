from tkinter import *
import tkinter.messagebox

def select_car_model_part1():
    global car_name
    car_name=StringVar(root)
    car_name.set('Select')
    selected_car_category=car_category.get()
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

def after_next():
    if car_name.get() in d:
        d.pop(car_name)
        userdetails()
        car_list.append(car_name)
        car_list.append(selected_car_category)
        print(car_list)
    else:
        tkinter.messagebox.showinfo("Car Unavailable", "Sorry! This car is already booked. Please select another car.")
    


#dictionary with car name and category, list for sql
    global d
d={"Mahindra Thar":"SUV", "Toyota Fortuner":"SUV", "Tata Harrier":"SUV",  "Hyundai Creta":"SUV", "Mahindra Scorpio":"SUV",
   "Maruti Swift Dzire":"Sedan", "Hyundai Verna":"Sedan", "Honda City":"Sedan",  "Tata Tigor":"Sedan", "Maruti Ciaz":"Sedan",
   "Tata Altroz":"Hatchback", "Maruti Swift":"Hatchback", "Hyundai Grand i10":"Hatchback",  "Tata Tiago":"Hatchback",
   "Maruti Celerio":"Hatchback"}
global car_list
car_list=[]
    
#root
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
selectcartype = Label(root, text = "Select Car type: ", bg="grey", fg="black", font="Times 18").place(x=150, y=220)


#droplist 1
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

car_model = Label(root, text = "Car Model:", bg="grey", fg="black", font="Times 16").place(x=150, y=400)

#button 2
nextbtn= Button(root, text="    Next    ", bg="black", fg="white", font="Times 16", command=after_next)
nextbtn.place(x=250, y=490)


root.mainloop()

