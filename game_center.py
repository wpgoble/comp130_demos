import random

# Asks user to pick an int to play rps
user = int(input("Pick [1]: Rock, [2]: Paper, or [3]: Scissors: "))
computer = random.randint(1, 3) # randomly picks computer choice

# Logic behind the game
if user == computer:
    print("You tied")
else:
    if user == 1:
        if computer == 2:
            print("You lose. Paper covers Rock")
        else:
            print("You win. Rock beats Scissors")
    elif user == 2:
        if computer == 3:
            print("You lose. Scissors cuts Paper")
        else:
            print("You win. Paper covers Rock")
    elif user == 3:
        if computer == 1:
            print("You lose. Rock beats Scissors")
        else:
            print("You win. Scissors cuts Paper")
