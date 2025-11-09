print("-- WELCOME TO Ambrosia Petrol --")
print()

Petrol = 1.40
Diesel = 1.55
LPG = 0.95
fuelType = 0
fuelName = ""

print("-- FUEL CHOICES --")
print()
print(f"Petrol costs {Petrol}")
print(f"Diesel costs {Diesel}")
print(f"LPG costs {LPG}")
print()
print("1. for Petrol")
print("2. for Diesel")
print("3. for LPG")
print()

fuelChoice = int(input("Enter in your choice: "))

if fuelChoice == 1:
    fuelType = Petrol
    fuelName = "Petrol"
elif fuelChoice == 2:
    fuelType = Diesel
    fuelName = "Diesel"
elif fuelChoice == 3:
    fuelType = LPG
    fuelName = "LPG"
else:
    print("Invalid choice, please try again.")
    exit()

print()

fuelAmount = float(input(f"Enter in how many litres of {fuelName} you would like: "))

preTotal = round(fuelAmount * fuelType, 2)
print(f"Your total is {preTotal}")

userPaid = float(input("Enter in how much you want to pay: "))
change = 0

if userPaid > preTotal:
    change = userPaid - preTotal
    print(f"Your change is {round(change, 2)}")
elif userPaid < preTotal:
    print("INSUFFICIENT FUNDS")
elif userPaid == preTotal:
    print("Accepted. Enjoy your fuel")