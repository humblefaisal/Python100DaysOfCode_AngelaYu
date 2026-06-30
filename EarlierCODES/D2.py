print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?  "))
tip=int(input("How much % tip would you like to give? 10,12 or 15? "))
split=int(input("Hpw many persons to split the bill? "))

print(f"Each person should pay : {round(bill*(1+0.01*tip)/split,2)}")
