import art
print(art.logo)

print("$$$ WELCOME TO THE GAME OF BLIND BID $$$")
bidlist={}
startbid=True

def calculate_bid(amountofbid):
    highestamount=0 # setting highest bid to 0 to compare it with bid amount
    winner=""
    for x in amountofbid: #amount of bid is bid list from function return value
        bidamount=bidlist[x] # cannot compare bidlist value / amount with highestamount so 1st taking value /amount from list using this operation
        if bidamount>highestamount: #then comparing it with highestbid amount
            highestamount=bidamount
            winner=x #will take the current bidder with highest value to enter if
    print(f"THIS IS THE HIGHEST BID {highestamount} , BY {winner.upper()}")

while startbid==True:
    name=input("enter your name: \n")
    bid=int(input("enter your bid amount : $"))
    bidlist[name] = bid

    move=input("is their anyone next to bid : yes or no \n").lower()
    if move=="yes":
        print("\n"*100)
    else:
        print("\n"*100)
        startbid=False
        calculate_bid(bidlist)

print("BYEE HAVE A NICE DAY")





