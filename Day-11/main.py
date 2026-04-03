import art
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10] #cards value from ace to king
game=input("Enter The GAme Of Black Jack yes or no : ")
# print(art.logo)
while game=="yes":
    print(art.logo)
    yourcard=random.choices(cards, k=2)                  # your card
    print(f"THIS IS YOUR CARD : {yourcard} \n TOTAL VALUE :{sum(yourcard)}")
    computercard=random.choices(cards,k=2)               # computer card
    print(f"THIS IS COMPUTERS CARD :{computercard[0]}")
    # print(sum(computercard))                            #understanding print computer card
    if sum(computercard)<12:
        computercard.append(random.choice(cards))         # computer appends if low card
        print(f"COMPUTER ADDED A CARD ")
    elif sum(computercard)>=15 and sum(computercard)<=17:
        computercard.append(random.choice(cards))
        print(f"COMPUTER ADDED A CARD ")

    else:
        pass
    addmore=True
    move=""
    while addmore:
        move=input("WOULD YOU LIKE TO ADD (yes or no): ").lower()         # you add card if you want
        if move=="yes":
            yourcard.append(random.choice(cards))
            print(yourcard)
            print(sum(yourcard))
        else :
            addmore=False

    if move=="no":                           # see result of your game
        gamemove=input("Would You Like To See The Result yes or no : ")
        if gamemove=="yes":
            print(f" YOUR TOTAL CARD {sum(yourcard)} \n COMPUTER TOTAL CARD {sum(computercard)} ")
            if sum(yourcard)>sum(computercard) and sum(yourcard)<=21:
                print(f"YOU WON !!")
            elif sum(yourcard)<sum(computercard) and sum(computercard)<=21:
                print(f" YOU LOST !! \n COMPUTER WON !!!")
            elif sum(yourcard)==sum(computercard):
                print(f"Draw \n {sum(yourcard)} = {sum(computercard)}")
            elif sum(yourcard)>21:
                print(f"YOU LOST !!")
                if sum(computercard)<=21:
                    print(f"COMPUTER WON {sum(computercard)} ")
            elif sum(computercard)>21:
                print(f"COMPUTER LOST")
                if sum(yourcard)<=21:
                    print(f"YOU WON {sum(yourcard)} ")

            else:
                pass

            newgame=input("NEW GAME yes or no : ")
            if newgame=="yes":
                print("\n"*10)
                pass
            else:
                game="no"
        else:
            newgame = input("start new game yes or no :")
            if newgame == "yes":
                print("\n" * 10)
                pass
            else:
                game="no"
    else:
        newgame = input("start new game yes or no :")
        if newgame == "yes":
            print("\n" * 10)
            pass
        else:
            game="no"


