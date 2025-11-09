month = input("Enter month: ").lower()

if month in ["december", "january", "february"]:
    print("Winter")
elif month in ["march", "april", "may"]:
    print("Spring")
elif month in ["june", "july", "august"]:
    print("Summer")
else:
    print("Autumn")
