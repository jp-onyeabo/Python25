# Write your code here :-)
#n1 = 9
#n2 = 3
#print(n1%n2)
#num = 0
#def fbCheck():
 #   if num%3 == 0:
  #      print("Fizz")
   # elif num%5 == 0:
        # print("Buzz")
    #elif num%5==0 and num%3 ==0:
    #    print("FizzBuzz")
    #else:
    #    print("Ngl idk bro")

#for i in range(0,100,1):
#    fb

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)