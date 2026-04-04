import art
import random
print(art.logo)
print("WELCOME \nTHE ROBOT IS THINKING OF A NUMBER BETWEEN 1 TO 100")
robotnumber=random.randint(1,100)
level=input("ENTER LEVEL 'EASY' OR 'HARD' : ").lower()

def gamelogic():        # to check number high or low with the robot number
    guessnum = int(input("START GUESING A NUMBER : "))
    if guessnum > robotnumber:
        print("GUESS TOO HIGH")
    elif guessnum < robotnumber:
        print("GUESS TOO LOW")
    elif guessnum == robotnumber:
        print("!!YOU GOT THE NUMBER!!")
        result="pass"
        return result
    else:
        pass

def level_easy():         # uses 10 attempts to guess the number level easy
    global robotnumber
    print("ENTER LEVEL EASY!! ")
    print("10 ATTEMPTS TO GUESS THE NUMBER")

    for x in range(10,1,-1):

        print("_________________________________________________")

        print(f"ATTEMPTS LEFT {x}")
        op=gamelogic()
        if op=="pass":
            return
    print(" ALL OF YOUR ATTEMPTS ARE USED \n YOU LOST !!")
    print(f"ROBOT GUESSES {robotnumber} !!")




def level_hard():          # uses 5 attempts to guess the robots number level hard
    global robotnumber
    print("ENTER LEVEL HARD!! ")
    print("5 ATTEMPTS TO GUESS THE NUMBER")

    for x in range(5,0,-1):

        print("_________________________________________________")
        print(f"ATTEMPTS LEFT {x}")
        op=gamelogic()      # game logic returns result when number is guessed to move out of the function
        if op=="pass":
            return
    print("ALL OF YOUR ATTEMPTS ARE USED \n!!YOU LOST !!")
    print(f"ROBOT GUESSES {robotnumber} !!")

if level=="easy":
    level_easy()
else:
    level_hard()
