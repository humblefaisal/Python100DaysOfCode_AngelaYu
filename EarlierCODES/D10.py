def add(a,b) :
    return a+b
def sub(a,b) :
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0 :
        return "Division by zero not allowed"
    return a/b
def calculator(func,a,b):
    return func(a,b)

operation = {"+":add,"-":sub,"*":mul,"/":div}
print("---Calculator---")
print("Available operations : + , - , * , /")
while True:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    op = input("Enter operation : ")
    if op in operation :
        result = calculator(operation[op],a,b)
        print(f"{a} {op} {b} = {result}")
    else :
        print("Invalid operation")

    more = input("Do you want to continue ? (y/n) : ")
    if more.lower() != 'y' :
        break
