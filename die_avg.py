import random


def dieRoll(sides):    
    result = random.randint(1, sides)
    return result


def die_avg():
    user = input("What size die? ")
    total = 0
    itr = 0
    while user.isdigit():
        side = int(user)
        roll = dieRoll(side)
        total += roll
        itr += 1
        user = input("What size die? ")
    avg = total / itr
    print(avg)
