litres = float(input("Enter tank size in litres: "))
current = float(input("Enter current nitrate level: "))
target = float(input("Enter target nitrate level: "))

dose = (current - target) * litres / 50
if dose <= 0:
    print("No dose needed")
else:
    print("Add", dose, "ml of nitrate remover")
