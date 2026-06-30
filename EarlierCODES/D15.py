#coffee machine

#dict for coffee- ingredients+cost : coffee : [water,coffee,milk,cost]
info={"espresso":[50,18,0,1.5],
      "latte":[200,24,150,2.5],
      "cappuccino":[250,24,100,3.0]}
index={0:"water",1:"coffee",2:"milk",3:"money"}
def has_enough_resources(order,resources):
    shortage=[]
    for i in range(3):
        if info[order][i]>resources[i]: 
            shortage.append(i)
    return shortage
def show_report(resources):
    print(f"Water : {resources[0]}ml")
    print(f"Coffee : {resources[1]}g")
    print(f"Milk : {resources[2]}ml")
    print(f"Money : ${resources[3]}")

if __name__=='__main__':
    water=300;coffee=100;milk=200;money=0.0
    while True:
        order=input("what is your order?(espresso/latte/cappuccino)")
        resources = (water,coffee,milk,money)
        if order == "exit": break
        if order == "report":
            show_report(resources)
            continue
        if order not in info: 
            print("Invalid demand!")
            continue
        resources_shortage = has_enough_resources(order,resources) 
        if len(resources_shortage)>0:
            apology=""
            for x in resources_shortage:
                apology += "Sorry. We do not have enough " + index[x] + "\n"
            print(apology)
            continue
        payment=0.0
        print("---Payment---")
        payment+=int(input("how many quaters?"))*0.25
        payment+=int(input("how many dimes?"))*0.10
        payment+=int(input("how many nickles?"))*0.05
        payment+=int(input("how many pennies?"))*0.01
        cost = info[order][3]
        if payment<cost:
            print(f"insuffcient payment! ${payment} Refunded")
            continue
        water-=info[order][0]
        coffee-=info[order][1]
        milk-=info[order][2]
        money+=cost
        if payment-cost>0:
            print(f"Succeeful purchase! Heres your ${payment-cost} change!")


