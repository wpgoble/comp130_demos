name = input("What is your name? ")

if len(name) <= 3:
    print("You have a short name")
elif len(name) >= 6:
    print("You have a long name")
else:
    print("You have a name")

print("Good-bye")
