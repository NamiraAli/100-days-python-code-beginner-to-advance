from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_IN_SEC = 25*60
SHORT_BREAK_SEC = 5*60
LONG_BREAK_SEC = 20*60
reps=0
tick="✔"
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)  #to stop the timer .after_cancel()
    canvas.itemconfig(timer_ticks,text="00:00") #to reset timer to 00:00
    label_timer.config(text="Timer")
    label_tick.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- #
# def start_timer():
#     count_down(100)


def start_timer_now():
    global reps
    reps+=1

    if reps % 8 == 0:
        count_down(LONG_BREAK_SEC)
        label_timer.config(text="LONG BREAK TIME", fg=GREEN)

    elif reps % 2 == 0 and reps < 8:
        count_down(SHORT_BREAK_SEC)
        label_timer.config(text="SHORT BREAK TIME", fg=PINK)

    else:
        count_down(WORK_IN_SEC)
        label_timer.config(text="WORKING TIME", fg=RED)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    #"00:00"
    global timer

    count_min=math.floor(count/60)
    count_sec=count%60

    if count_sec==0:
        count_sec="00"
    if len(str(count_sec))<2:
        count_sec="0"+str(count_sec)

    canvas.itemconfig(timer_ticks,text=f"{count_min}:{count_sec}") #to  edit canvas based text use itemconfig()
    if count > 0:
        timer=window.after(1000,count_down,count-1)
    else:
        newtick=""
        worksession=math.floor(reps/2)  # 1 ,2, 3,4
        start_timer_now()
        for x in range(worksession):
            newtick+=tick
        label_tick.config(text=newtick)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro NA")
window.config(padx=100,pady=50,bg=YELLOW)
#tkinter canva widgets to place img on window

canvas = Canvas(width=200, height=224, bg=YELLOW,highlightthickness=0)  # highlighttickness=0 to make the border of the image gone before applying this we could see a border around the img
tomato_img=PhotoImage(file="tomato.png") #the location of the image must be relevant to main.py here tomato is in same folder as main
canvas.create_image(100, 112, image=tomato_img) #here first we need to collect the image using PhotoImage #then the collected image is used here in create_image
timer_ticks=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

#colorhunt to use color pallate to get hexcode

#text

label_timer=Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,highlightthickness=0,bg=YELLOW)
label_timer.grid(row=0,column=1)

button_start=Button(text="Start",font=(FONT_NAME,15,"bold"),fg=RED,command=start_timer_now) #fg for text color foreground
button_start.grid(row=2,column=0)
button_reset=Button(text="Reset",font=(FONT_NAME,15,"bold"),fg=RED,command=reset_timer)
button_reset.grid(row=2,column=2)

label_tick=Label(font=(FONT_NAME,15,"bold"),fg=GREEN,bg=YELLOW)
label_tick.grid(row=3,column=1)



canvas.grid(row=1,column=1)

window.mainloop()
