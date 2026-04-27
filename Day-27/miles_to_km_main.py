from tkinter import *



def onclick_calculate():
    miles_value=float(input_mile.get()) #store the miles value
    km=round(miles_value * 1.609)
    km_value.config(text=km)


#window
window=Tk()
window.title("Mile To Km Calculator _ NA")
window.minsize(width=300,height=200)
window.config(padx=10,pady=10)

#topic
topic=Label(text="Miles to Km",font=("Times New Roman",10,"bold"))
topic.pack()
topic.grid(row=0,column=0)


#entry
input_mile=Entry(width=10,font=("Times New Roman",7))
input_mile.grid(row=0,column=2)


#label
isequalto=Label(text="IS Equal To ",font=("Times New Roman",10))
isequalto.grid(row=1,column=1)

miles=Label(text=" Miles",font=("Times New Roman",10))
miles.grid(row=0,column=3)


km=Label(text=" KM",font=("Times New Roman",10))
km.grid(row=1,column=3)

km_value=Label(text="0",font=("Times New Roman",10))
km_value.grid(row=1,column=2)

#button
calculate=Button(text="Calculate",font=("Times New Roman",10),command=onclick_calculate)
calculate.grid(row=2,column=2)


window.mainloop()
