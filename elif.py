savings = float(input("Enter how much you have in savings: "))

if savings == 0:
    print("Sorry no savings")
elif savings < 500:
    print("Well done")
elif savings < 1000:
    print("That's a good some!")
elif savings < 10000:
    print("That's a lot of money")
else:
    print("Thanks for trying")

