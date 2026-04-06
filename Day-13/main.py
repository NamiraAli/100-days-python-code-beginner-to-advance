import random
import game_data
import art

print(art.logo)

game_over=True
value1 = random.choice(game_data.data)
countvalue1 = value1["follower_count"]
score=0

while game_over:
    value2 = random.choice(game_data.data)
    countvalue1 = value1["follower_count"]
    countvalue2=value2["follower_count"]
    def play_game(value1,value2):
        global game_over
        global score
        print(f"option A :{value1["name"] , value1["description"], value1["country"]}")
        print(f"option B :{value2["name"] , value2["description"], value2["country"]}")


        choose_which_value_is_greater=input("choose which value is greater A OR B: ")
        if choose_which_value_is_greater == "A":

            if countvalue1>countvalue2: # 145>85
                score+=1
                print(f"YOU GUESSED CORRECT")
                print(f"Your Score {score}")
                print(f"{value1["name"],value1["follower_count"]} >>>> {value2["name"],value2["follower_count"]}")
                print("---------------------------------------------")
                return value2
            else:
                print(f"YOU GUESSED WRONG {value2["name"],value2["follower_count"]} HAS MORE FOLLOWERS THAN {value1["name"],value1["follower_count"]} !! ")
                print("---------------------------------------------")
                game_over=False

        elif choose_which_value_is_greater == "B":
            if countvalue1<countvalue2: # 138<167
                score+=1
                print(f"YOU GUESSED CORRECT")
                print(f"Your Score {score}")

                print(f"{value2["name"],value2["follower_count"]} >>>> {value1["name"],value1["follower_count"]}")

                print("---------------------------------------------")
                return value2
            else:
                print(f"YOU GUESSED WRONG {value1["name"],value1["follower_count"]} HAS MORE FOLLOWERS THAN {value2["name"],value2["follower_count"]} !! ")
                print("---------------------------------------------")
                game_over=False
        elif countvalue2==countvalue1:
            pass
            return value2

        else:
            print("choose between A or B ")

        return value2

    value1=play_game(value1=value1,value2=value2)

print(f"Your Total Score is {score}")

