from quiz_brain import Quiz
from question_model import Question
from data import question_data

question_bank=[]
for x in question_data:
    question_text=x["text"] #take 1st dict ie in x from that text value
    question_ans=x["answer"]
    new_q=Question(question_text,question_ans) #the list data is converted to obj ie new_q
    question_bank.append(new_q)

# print(question_bank[0].quetext) # question_bank is a list from that list take 0th position value their are 2 values in 0 ie text,answer
# # we are using quetext because we have obj new_q from Question class where we have used quetext as an attribute
# #to get the text from questionbank list we use (question_bank[0].quetext)
# print(question_bank[0].ans)

quiz=Quiz(question_bank)
while quiz.still_has_question(): #alwyas use obj name "." and then function name to use that function from that class if we import that class
    #here quiz is the obj of class Quiz and to use function or method from class Quiz we need to use by first using obj name
    #eg. quiz.methodname
    quiz.next_question()
print("QUIZ END")
print(f"FINAL SCORE IS {quiz.score}/ {len(question_bank)}")
