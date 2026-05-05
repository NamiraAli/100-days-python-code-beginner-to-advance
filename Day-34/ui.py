from quiz_brain import QuizBrain
from tkinter import *
THEME_COLOR = "#375362"
# THEME_COLOR = "#895162"
FONT=("Arial", 15, "italic")

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quiziess")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)

        self.canvas=Canvas(self.window,width=300,height=250,bg="white")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)

        self.question_text=self.canvas.create_text(150,125,text="question here",width=280,fill=THEME_COLOR,font=FONT)
        # 150 and 125 are halves of widht and height of canvas  no need for grid here


        self.score_label=Label(self.window,text="Score:",bg=THEME_COLOR,fg="white",font=("Arial",15,"bold"))
        self.score_label.grid(row=0,column=1)
        right=PhotoImage(file="images/true.png")
        wrong=PhotoImage(file="images/false.png")



        self.right_buttton=Button(image=right,bg=THEME_COLOR,highlightthickness=0,command=self.true_check_ans)
        self.right_buttton.grid(row=2,column=0)

        self.wrong_buttton = Button(image=wrong, bg=THEME_COLOR, highlightthickness=0,command=self.false_check_ans)
        self.wrong_buttton.grid(row=2, column=1)

        self.get_next_question()




        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"THE END \n FINAL SCORE : {self.quiz.score}")

            self.right_buttton.config(state="disabled")
            self.wrong_buttton.config(state="disabled")


    def true_check_ans(self):
        is_right=self.quiz.check_answer("True")
        self.feedback(is_right)


    def false_check_ans(self):
        is_right=self.quiz.check_answer("False")

        self.feedback(is_right)

    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)
