import random

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

print("1) Rock\n2) Paper\n3) Scissors")

try:
    player = int(input("Enter your choice (1-3): "))
    if player not in choices:
        print("Invalid choice. Please enter 1, 2, or 3.")
        exit()

    computer = random.randint(1, 3)

    print(f"\nYou chose: {choices[player]}")
    print(f"Computer chose: {choices[computer]}")

    if player == computer:
        print("It's a tie!")
    elif (player - computer) % 3 == 1:
        print("You win!")
    else:
        print("You lose! Better luck next time!")

except ValueError:
    print("Invalid input. Please enter a number between 1 and 3.")
