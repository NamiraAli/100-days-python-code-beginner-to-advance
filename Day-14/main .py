import data

TOTALEARN=0
forcustomer=True


def ingredients_management():
    # print(data.resources)
    data.resources["water"]=data.resources["water"]-data.MENU[which_coffee]["ingredients"]["water"]
    data.resources["milk"]=data.resources["milk"]-data.MENU[which_coffee]["ingredients"]["milk"]
    data.resources["coffee"]=data.resources["coffee"]-data.MENU[which_coffee]["ingredients"]["coffee"]
    return data.resources

def addmoney():
    global TOTALEARN
    money=int(input("INSERT YOUR MONEY : "))
    if money<data.MENU[which_coffee]["cost"]:
        print(f"YOU PAID LESS AMOUNT , HERE IS YOUR REFUND {money}")
    else:
        change=money-data.MENU[which_coffee]["cost"]
        print(f" THIS IS YOUR CHANGE {change}")
        TOTALEARN+=data.MENU[which_coffee]["cost"]
        print(f"GALLA : {TOTALEARN}")

def res_insufficient():
    if data.resources["water"]<data.MENU[which_coffee]["ingredients"]["water"]:
        print("WE GOT LESS RESOURCES FOR YOUR COFFEE !!! \n SORRY!")
        return
    elif data.resources["milk"]<data.MENU[which_coffee]["ingredients"]["milk"]:
        print("WE GOT LESS RESOURCES FOR YOUR COFFEE !!! \n SORRY!")
    elif data.resources["coffee"]<data.MENU[which_coffee]["ingredients"]["coffee"]:
        print("WE GOT LESS RESOURCES FOR YOUR COFFEE !!! \n SORRY!")
    else:
        addmoney()
        pass




want_coffee=True
while want_coffee:


    number = 0


    move=input("WOULD YOU LIKE TO HAVE A COFFEE ?? YES OR NO : ").lower()
    if move=="yes":
        print("**********MENU**********")
        for x in data.MENU:
            number += 1
            print(number, x)

        which_coffee = input("ENTER YOUR COFFEE CHOICE : ").lower()

        if which_coffee=="espresso":

            print(f"COST FOR 1 ESPRESSO : {data.MENU["espresso"]["cost"]}")
            res_insufficient()
            updateingriedients=ingredients_management()


            # print(updateingriedients)
        elif which_coffee=="latte":

            print(f"COST FOR 1 LATTE : {data.MENU["latte"]["cost"]}")
            res_insufficient()
            updateingriedients=ingredients_management()


            # print(updateingriedients)
        elif which_coffee=="cappuccino":

            print(f"COST FOR 1 CAPPUCCINO : {data.MENU["cappuccino"]["cost"]}")
            res_insufficient()
            updateingriedients=ingredients_management()

        else:
            print("THIS OPTION IS NOT IN THE MENU PLEASE TYPE CORRECT ORDER ")



    elif move=="no":
        want_coffee = False

    elif move=="report":

        print("\n"*30)
        print("############## REPORT ##############")
        print(f"TODAYS TOTAL EARNING    :   {TOTALEARN}")
        print(f"RESOURCES LEFT          :   {data.resources}")

    elif move=="add":

        print("\n"*30)
        print("############## ADD RESOURCES ##############")
        water=int(input("QUANTITY OF WATER TO BE ADDED : "))
        data.resources["water"]+=water
        milk=int(input("QUANTITY OF MILK TO BE ADDED : "))
        data.resources["milk"]+=milk
        coffee=int(input("QUANTITY OF COFFEE TO BE ADDED : "))
        data.resources["coffee"]+=coffee




