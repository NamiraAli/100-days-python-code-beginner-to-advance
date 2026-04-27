from tkinter import *


def buttonclick():
    # my_label.config(text="You clicked me") #this will also print the text no need to use print
    my_label.config(text=input.get()) #this will also print the text no need to use print




# window = tkinter.Tk() #cause we imported * all modules from tkinter no need to specify tkinter now
window = Tk() #so we use this type
window.title("My First GUI")
window.minsize(400,300)
window.config(padx=20,pady=20) #padding on x and y in window



#Label
my_label=Label(text="I am a label", font=("Ariel",20,"italic"))  # to create a label call Label()
# my_label.pack(side="left") #to make the label appear in center #if not used pack() nothing will show up
# my_label.pac k(side="left")
# my_label.pack(expand=True)  #use these type of attributes to move around the label
# my_label.place(x=100,y=200)

my_label.grid(row=0, column=0)
# my_label["text"]="new text"
my_label.config(text="new text") #to change the text of my_label use config()
my_label.config(padx=20,pady=20)  #adding padding around widgets here it is label
#button
button= Button(text="Click me",command=buttonclick) #command use for function
# button.pack(side="left")
button.grid(row=1, column=1)
button1=Button(text="new button",command=buttonclick)
button1.grid(row=0,column=2)

#entry
input=Entry(width=10)
input.grid(row=2, column=3) #when using grid we cannot use pack and vise versa
# input.pack(side="left")
# input.get() #this get hold of the input value from Entry class




window.mainloop() #this keeps the window open mainloop() function
