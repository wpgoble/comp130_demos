import random

user = int(input("Pick [1]: Rock, [2]: Paper, or [3]: Scissors: "))
computer = random.randint(1, 3)

# We want to user 1, 2, 3 for R, P, S
# Rock -> 1
# Paper -> 2
# Scissors -> 3
# if user == computer:
#    print("You tie")
# elif user == 1 and computer == 3:
#    print("You win")
# elif user == 1 and computer == 2:
#    print("You lose")
# elif user == 2 and computer == 1:
#    print("You win")
# elif user == 2 and computer == 3:
#    print("You lose")
# elif user == 3 and computer == 2:
#    print("You win")
# elif user == 3 and computer == 1:
#    print("You lose")
if user == computer:
    print("You tied")
else:
    if user == 1:
        if computer == 2:
            print("You lose")
        else:
            print("You win")
