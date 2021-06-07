import random
x = random.randint(0,100)
while True:
    y = int(input("Jaką wylosowałem liczbę?\n"))
    if y<x:
        print("Za mała!")
    elif y>x:
        print("Za duża")
    elif y==x:
        print("Brawo trafiłeś!")
        break