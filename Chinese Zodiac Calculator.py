c='y'
while c=='y':
    a = int(input("Enter your year: "))
    b = a % 12

    if b == 0:
      z = "Monkey"
    elif b == 1:
      z = "Rooster"
    elif b == 2:
      z = "Dog"
    elif b == 3:
      z = "Pig"
    elif b == 4:
      z = "Rat"
    elif b == 5:
      z = "Ox"
    elif b == 6:
      z = "Tiger"
    elif b == 7:
      z = "Rabbit"
    elif b == 8:
      z = "Dragon"
    elif b == 9:
      z = "Snake"
    elif b == 10:
      z = "Horse"
    elif b == 11:
      z = "Sheep"

    print("Your Chinese Zodiac sign is:", z)
    
