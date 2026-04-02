import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def mod(n1,n2):
    return n1%n2

operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "%":mod
}
n1=int(input("enter your value 1 : "))
play=True
while play:

    n2 = int(input("enter your value 2 : "))
    for x in operation:
        print(x)
    userinput=input("enter what you want to perform : ")
    if userinput != "+" and userinput != "-" and userinput != "*" and userinput != "/" and userinput != "%":
        print("enter valid symbol babes !! ")
        play=False

    else:
        result=operation[userinput](n1,n2)
        print(f"THIS IS THE RESULT \n {n1} {userinput} {n2} = {result}")
        gameover=input("WOULD YOU LIKE TO END THE PROGRAM YES OR NO : ").lower()
        if gameover == "yes":
            print("CALCULATOR CLOSE")
            play=False
        else:
            nextuse=input("WOULD YOU LIKE TO USE THE SAME NUMBER AS INPUT YES OR NO : ").lower()
            if nextuse =="yes":
                n1=result
            else:
                n1 = int(input("enter your value 1 : "))



