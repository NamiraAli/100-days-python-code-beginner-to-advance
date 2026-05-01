from tkinter import *
from tkinter import messagebox
import pyperclip
import json


font=("Times New Roman",18)
font_button=("Times New Roman",10)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    no_letters=random.randint(7,10)
    no_numbers=random.randint(2,4)
    no_symbols=random.randint(1,3)

    password_list=[]

    for x in range(no_letters):
        password_list.append(random.choice(letters))

    for x in range(no_numbers):
        password_list.append(random.choice(numbers))

    for x in range(no_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    # mypassword = ""
    # for x in password_list:
    #     mypassword += x

    mypassword="".join(password_list)
    #enter to entry_pass
    entry_pass.insert(0,mypassword)
    pyperclip.copy(mypassword) #to automatically copy the password




# ---------------------------- SAVE PASSWORD ------------------------------- #
def click_add():
    website=entry_website.get() #.get() to catch the input
    email=entry_email.get()
    password=entry_pass.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }

    if website=="" or email=="" or password=="":
        messagebox.showerror("Error","Please fill all fields")
    else:
        #write and update data in json + error management
        try:
            with open("password_manager.json") as file: #we open the json in read mode though no such fole exists
                data=json.load(file) #it canot load the data ie read the data error occurs
                #so jump onto except block

        except FileNotFoundError:
            with open("password_manager.json","w") as file:
                json.dump(new_data,file,indent=4) #we create a new file "w" and dump the input data in the file
            data=new_data #the data we entered now is stored in data cause error occured
        else:
            data.update(new_data) #this works when error not occur and try is successful
            with open("password_manager.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally: #will work eventually
           #no matter what it will clear the entry
            entry_website.delete(0, "end")  # .delete() to delete the text
            entry_pass.delete(0, "end")
        # messagebox.showinfo("Success","Password has been added!")

        #entry saved in password manager in txt
                 # messagebox.askokcancel(title=website,message=f"email: {email} \n password: {password}")
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def searchpass():
    website = entry_website.get()  # .get() to catch the input
    email = entry_email.get()
    password = entry_pass.get()
    try:
        with open("password_manager.json","r") as searchfile:
            data=json.load(searchfile)
    except FileNotFoundError:
        messagebox.showerror("Error","File not found")
    else:
        if website in data:
            # print(data[website]["email"])
            messagebox.showinfo(title="password",
                                message=f"website : {website} \n email : {data[website]["email"]} \n password : {data[website]["password"]}")
        else:
            messagebox.showerror("Error", f"The {website} is Not is the list")


# messagebox.showinfo("Success","Password has been added!")


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
# window.minsize(500,500)
window.config(padx=50,pady=50)
window.title("PASSWORD MANAGER")

canvas=Canvas(height=200,width=200)
img1=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img1)
canvas.grid(row=0,column=1)


#Labels
label_website=Label(text="Website : ",font=font)
label_website.grid(row=1,column=0,sticky="e")  #sticky="e" to align the text to right

label_email=Label(text="Email/Username : ",font=font)
label_email.grid(row=2,column=0,sticky="e")

label_password=Label(text="Password : ",font=font)
label_password.grid(row=3,column=0,sticky="e")

#buttons
button_generatepass=Button(text="Generate Password",font=font_button,command=generate_pass)
button_generatepass.grid(row=3,column=2,sticky="e")

button_add=Button(text="Add",font=font_button,command=click_add)
button_add.grid(row=4,column=1)

button_search=Button(text="Search",width=10,font=font_button,command=searchpass)
button_search.grid(row=1,column=3,sticky="w",padx=10)

#entry
entry_website=Entry(width=34,font=font)
entry_email=Entry(width=35,font=font)
entry_website.grid(row=1,column=1,columnspan=2)
entry_website.focus() #to get the cursor to start here

entry_email=Entry(width=35,font=font)
entry_email.grid(row=2,column=1,columnspan=2)
entry_email.insert(0,"namiraali@gmail.com") #use END to get text at end and 0 to get in front


entry_pass=Entry(width=21,font=font)
entry_pass.grid(row=3,column=1,sticky="w")


window.mainloop()
