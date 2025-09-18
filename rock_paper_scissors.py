import random

print("1) Rock")
print("2) Paper")
print("3) Scissors")

player = int(input("Enter your choice (1-3): "))
computer = random.randint(1, 3)

if player == computer:
    print("It's a tie!")
elif (player == 1 and computer == 3):
    print("You win! Rock crushes Scissors.")
elif (player == 2 and computer == 1):
    print("You win! Paper covers Rock.")
elif (player == 3 and computer == 2):
    print("You win! Scissors cut Paper.")
else:
    print("You lose! Better luck next time!")