number = int(input("Please provide a whole number: "))

if number % 3 == 0:
    print(f"{number} is a multiple of 3")
elif number % 5 == 0:
    print(f"{number} is a multiple of 5")
elif number % 15 == 0:
    print(number, "is a multiple of 15")
else:
    print(number, "is a number")
