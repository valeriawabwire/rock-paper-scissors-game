import random

options = ("rock", "paper", "scissors")
running = True

while running:
    computer = random.choice(options)
    player = None
    attempts = 3 

    while player not in options and attempts > 0:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
        if player not in options:
            attempts -= 1
            if attempts > 0:
                print(f"Invalid choice. You have {attempts} attempts left.")
            else:
                print("No attempts left. Moving to next round.")
                player = None  # Reset player to None if no valid choice made

    if player:  # Proceed only if a valid choice was made
        print(f"player: {player}")
        print(f"computer: {computer}")

        if player == computer:
            print("You Tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("You lose!")
    else:
        print("No valid choice made this round.")

    if input("Do you want to play again (y/n): ").lower() != "y":
        running = False
        print("Thank you for playing!")