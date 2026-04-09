# from main import question_bank, new_q
# from data import question_data


class Quiz:
    def __init__(self,q_list):
        self.q_number=0
        self.score=0
        self.question_list=q_list

    def still_has_question(self):
        # if self.question_list[self.q_number]== self.question_list[-1]:
        #     return False
        # else:
        #     return True
        if self.q_number<len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question=self.question_list[self.q_number]
        self.q_number+=1
        user_answer=input(f"Q.{self.q_number} {current_question.text} (True//False) :")
        self.check_answer(user_answer,current_question.ans)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("you got right")
            self.score+=1

        else:
            print("wrong answer")
        print(f"correct answer: {correct_answer}")
        print(f"your score {self.score} / {self.q_number}")
        print("*******************************************************\n")

