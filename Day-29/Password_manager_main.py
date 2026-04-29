from tkinter import *
from tkinter import messagebox
import pyperclip


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

    if website=="" or email=="" or password=="":
        messagebox.showerror("Error","Please fill all fields")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"email: {email} \n password: {password}")

        if is_ok:
            #entry saved in password manager in txt
            with open("password_manager.txt","a") as file:
                file.write(website + " | " + email + " | " + password + "\n")

                #delete item when click (it must be in with open : cause if the data is added to file it deltes the text
                entry_website.delete(0,"end") #.delete() to delete the text
                # entry_email.delete(0,"end")
                entry_pass.delete(0,"end")
            # messagebox.showinfo("Success","Password has been added!")
        # messagebox.askokcancel(title=website,message=f"email: {email} \n password: {password}")
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

#entry
entry_website=Entry(width=35,font=font)
entry_email=Entry(width=35,font=font)
entry_website.grid(row=1,column=1,columnspan=2)
entry_website.focus() #to get the cursor to start here

entry_email=Entry(width=35,font=font)
entry_email.grid(row=2,column=1,columnspan=2)
entry_email.insert(0,"namiraali@gmail.com") #use END to get text at end and 0 to get in front


entry_pass=Entry(width=21,font=font)
entry_pass.grid(row=3,column=1,sticky="w")


window.mainloop()
