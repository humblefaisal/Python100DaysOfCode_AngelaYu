from D15 import info
class Item:
    def __init__(self,name,water,coffee,milk,cost):
        self.name=name
        self.water=water
        self.coffee=coffee
        self.milk=milk
        self.cost=cost
    
class Resources:
    def __init__(self,q_water=300,q_coffee=100,q_milk=200):
        self.q_water=q_water
        self.q_coffee=q_coffee
        self.q_milk=q_milk
        # self.q_money=q_money
    def is_resources_enough(self,item):
        shortage=[]
        if item.water>self.q_water:
            shortage.append("Water")
        if item.coffee>self.q_coffee:
            shortage.append("Coffee")
        if item.milk>self.q_milk:
            shortage.append("Milk")
        return shortage
    def use_resource(self,item):
        self.q_water-=item.water
        self.q_coffee-=item.coffee
        self.q_milk-=item.milk
    def report(self):
        return self.__str__()
    def __str__(self):
        return f"Milk : {self.q_milk}ml\nWater : {self.q_water}ml\nCoffee : {self.q_coffee}g\n"

class Money:
    def __init__(self,quater=0,dimes=0,nickles=0,pennies=0):
        self.money=0
        self.money+=quater*0.25
        self.money+=dimes*0.1
        self.money+=nickles*0.05
        self.money+=pennies*0.01
    def get_val(self):
        return self.money
    def dec_amt(self,amt):
        self.money-=amt
    def inc_amt(self,amt):
        self.money+=amt
    def __str__(self):
        return f"${self.get_val():.2f}"

class Manager:
    def __init__(self,menu,resources,money):
        self.menu={v.name:v for v in menu }
        self.resources=resources
        self.money=money
    def system(self):
        while True:
            order=input("what is your order?(espresso/latte/cappuccino)")
            if order == "exit": break
            if order == "report": 
                print(self.report())
                print(f"Money : {self.money}")
                continue
            if order == "refill":
                self.refill()
                continue
            if order not in self.menu :
                print("Invalid request")
                continue
            self.take_order(self.menu[order])
        return

    def take_order(self,item):
        shortage = self.resources.is_resources_enough(item)
        if len(shortage) > 0:
            print(f"Sorry. We do not have {shortage} in enough quantity.")
            return False
        else :
            print(f"Your order for {item.name} is ready. procced for payment")
        if not self.take_payment(item.cost):
            return False
        self.resources.use_resource(item)
        self.money.inc_amt(item.cost)

    def take_payment(self,cost):
        print("---Payment---")
        payment = Money(int(input("how many quaters?")),int(input("how many dimes?")),int(input("how many nickles?")),int(input("how many pennies?")))
        if payment.get_val() < cost:
            print("Sorry you have insufficient amt!")
            return False
        payment.dec_amt(cost)
        print(f"Successfull purchase. Here's your change of {payment}")
        return True
    
    def report(self):
        return self.resources.report()
    def refill(self):
        self.resources = Resources()

if __name__=='__main__':
    menu = []
    for name,req in info.items():
        item = Item(name,req[0],req[1],req[2],req[3])
        menu.append(item)
    res = Resources()
    money = Money()
    manager = Manager(menu=menu,resources=res,money=money)
    manager.system()

