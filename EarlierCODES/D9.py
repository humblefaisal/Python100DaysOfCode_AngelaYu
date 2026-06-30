from os import system
bid = {}
more=True
while more:
    name = input("Enter your name : ")
    bid_money = int(input("Enter your bid (INR):"))
    bid[name]=bid_money
    more=input("Are there more people?(y/n)") == "y"
    system("cls")

name=""
bid_money=0
for key,val in bid.items():
    if val>bid_money:
        name=key
        bid_money=val

print("Our winner is "+ name + f" with bid money : {bid_money}")


# d = {x:x*x for x in range(0,5)}
# for key,val in d.items():
#     print(f"{key} : {val}")
