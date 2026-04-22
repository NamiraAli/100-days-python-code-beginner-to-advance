import turtle
import pandas
screen=turtle.Screen()
screen.title("INDIA STATES NAME")
img="India-state.gif"
screen.addshape(img)
turtle.shape(img)


#to know the cordinate of the area on screen
# def get_mouse(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse)
# turtle.mainloop() #keeps the screen open as exitonclick does
# #but does not et on click



data = pandas.read_csv("states_data.csv")
guessed_state=[]
while len(guessed_state) < 29:
    user_input=screen.textinput(title=f"{len(guessed_state)} / 29 ",prompt="Enter State name : ").title()
    # print(user_input)

    check_states=data.state.to_list()
    # print(check_states)
    if user_input in check_states:
        guessed_state.append(user_input)
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        row_state_data=data[data.state==user_input] #pulls out the row
        t.goto(row_state_data.x.item(),row_state_data.y.item())
        # t.write(user_input)
        t.write(row_state_data.state.item())   # pulls out from row_state_data the state box the value
    if user_input == "Exit":
        not_guessed_state=[]
        for x in check_states:
            if x in guessed_state:
                pass
            else:
                not_guessed_state.append(x)
        print(not_guessed_state)
        df=pandas.DataFrame(not_guessed_state) # its like creating a table
        df.to_csv("not_guessed_states.csv")

        break


screen.exitonclick()





