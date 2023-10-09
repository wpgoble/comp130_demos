import random

game_name = input("Please select from these games: [1] rps, [2] totality ")
game_name = int(game_name)

# play rock, paper, scissors
if game_name == 1:
    player1_points = 0
    computer_points = 0

    for charlie in range(3):
        if (player1_points == 2 and computers_points == 0) or (computer_points == 2 and player1_points == 0):
            break
        
        # Asks user to pick an int to play rps
        user = int(input("Pick [1]: Rock, [2]: Paper, or [3]: Scissors: "))
        computer = random.randint(1, 3) # randomly picks computer choice            

        # Logic behind the game 
        if user == computer:
            print("You tied")
            player1_points += 1
            computer_points += 1
        else:
            if user == 1:
                if computer == 2:
                    print("You lose. Paper covers Rock")
                    computer_points += 1
                else:
                    print("You win. Rock beats Scissors")
                    player1_points += 1
            elif user == 2:
                if computer == 3:
                    print("You lose. Scissors cuts Paper")
                    computer_points += 1
                else:
                    print("You win. Paper covers Rock")
                    player1_points += 1
            elif user == 3:
                if computer == 1:
                    print("You lose. Rock beats Scissors")
                    computer_points += 1
                else:
                    print("You win. Scissors cuts Paper")
                    player1_points += 1

    if player1_points == computer_points:
        print("You tied")
    else:
        if player1_points > computer_points:
            print(f"Congrats you win! {player1_points} vs {computer_points}")
        else:
            print("You lost to a computer")

# now we can play totality
elif game_name == 2:
    print("Welcome to totality! To play you will roll 3 die and tally the score.")
    print("The highest score wins. If two die have the same vlaue, we multiply ")
    print("instead of add.")

    player1_name = input("Player 1, what is your name? ")
    player2_name = input("Player 2, what is your name? ")

    # figure out player 1
    player1_score = 0
    p1_d1 = random.randint(1, 6)
    p1_d2 = random.randint(1, 6)
    p1_d3 = random.randint(1, 6)

    if p1_d1 == p1_d2 == p1_d3:
        player1_score = p1_d1**3
    elif p1_d1 == p1_d2:
        player1_score = p1_d1**2 + p1_d3
    elif p1_d1 == p1_d3:
        player1_score = p1_d1**2 + p1_d2
    elif p1_d3 == p1_d2:
        player1_score = p1_d2**2 + p1_d1
    else:
        player1_score = p1_d1 + p1_d2 + p1_d3

    # figure out player 2
    player2_score = 0
    p2_d1 = random.randint(1, 6)
    p2_d2 = random.randint(1, 6)
    p2_d3 = random.randint(1, 6)

    if p2_d1 == p2_d2 == p2_d3:
        player2_score = p2_d1**3
    elif p2_d1 == p2_d2:
        player2_score = p2_d1**2 + p2_d3
    elif p2_d1 == p2_d3:
        player2_score = p2_d1**2 + p2_d2
    elif p2_d3 == p2_d2:
        player2_score = p2_d2**2 + p2_d1
    else:
        player2_score = p2_d1 + p2_d2 + p2_d3
        

    if player1_score == player2_score:
        print("You tied")
    else:
        if player1_score > player2_score:
            print(f"{player1_name} wins!")
        else:
            print(f"{player2_name} wins!")

















    
    
