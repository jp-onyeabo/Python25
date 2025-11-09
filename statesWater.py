#Celsius for normal people again
temp = float(input("Enter temperature in °C: "))

if temp <= 0:
    print("Solid (Ice)")
elif temp < 100:
    print("Liquid (Water)")
else:
    print("Gas (Steam)")
