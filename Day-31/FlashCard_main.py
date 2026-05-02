from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data=pandas.read_csv("data/Arabic_English.csv")
new_data=data.to_dict("records")
word_known=pandas.read_csv("data/words_learned.csv")
my_words=word_known.to_dict("records")
word=[]


def getword(): #when click wrong
    global fliptimer
    window.after_cancel(fliptimer)
    current_data=random.choice(new_data)
    if current_data in my_words:
        new_data.remove(current_data)
        current_data = random.choice(new_data)
        word.append(current_data)
    else:
        word.append(current_data)

    # print(word)
    canvas.itemconfig(canvas_image,image=card_back)
    canvas.itemconfig(head, text="Arabic",fill="white")
    canvas.itemconfig(arabic_word, text=current_data["Arabic"],fill="white")
    fliptimer=window.after(3000, func=changecard)


def changecard(): #when click right

    canvas.itemconfig(canvas_image, image=card_front)
    try:
        canvas.itemconfig(arabic_word,text=word[-1]["English"],fill="black")
    except IndexError:
        canvas.itemconfig(head, text="English", fill="black")
    else:
        canvas.itemconfig(head, text="English", fill="black")
    finally:
        global fliptimer
        window.after_cancel(fliptimer)
        fliptimer = window.after(3000, func=changecard)
        # fliptimer = window.after(3000, func=getword) # if you want to again flip the card back to arabic then use this


def i_know_the_word():
    if word:
        current_word = word[-1]

        my_words.append(current_word)
        new_data.remove(current_word)

        df = pandas.DataFrame(my_words)
        df.to_csv("data/words_learned.csv", index=False)

        getword()


#ui

window = Tk()
window.title("Flash-Cards")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
# window.minsize(500,500)
fliptimer=window.after(3000,func=changecard)


canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

card_back=PhotoImage(file="images/card_back.png")
card_front=PhotoImage(file="images/card_front.png")
canvas_image=canvas.create_image(400, 263,image=card_back)
canvas.grid(row=0,column=0,columnspan=2)


#buttons
wrong_button_pic = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_pic, highlightthickness=0,command=getword)
wrong_button.grid(row=1,column=0)

right_button_pic = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_pic, highlightthickness=0,command=i_know_the_word)
right_button.grid(row=1,column=1)


#label
head=canvas.create_text(400,150,text="Arabic",font=("Ariel",40,"italic"),fill="white")
canvas.grid(row=0,column=0,columnspan=2)

arabic_word=canvas.create_text(403,263,text="Word",font=("Ariel",50,"bold"),fill="white")
canvas.grid(row=0,column=0,columnspan=2)



window.mainloop()
