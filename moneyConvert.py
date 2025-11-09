#

gbp = float(input("Enter amount in GBP: "))
currency = input("Convert to (USD/EUR/YUAN/YEN): ").lower()

if currency == "usd":
    print(gbp * 1.25)
elif currency == "eur":
    print(gbp * 1.15)
elif currency == "yuan":
    print(gbp * 9.1)
elif currency == "yen":
    print(gbp * 180)
else:
    print("Invalid currency")
