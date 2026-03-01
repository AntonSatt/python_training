import random

choices = ["rock", "paper", "scissors"]

wins = 0
losses = 0
draws = 0

print("Rock, Paper, Scissors! (or 'q' to quit)")

while True:
    player = input("\nYour move: ").lower().strip()

    if player == "q":
        break

    if player not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a draw!")
        draws += 1
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You win!  ✓")
        wins += 1
    else:
        print("Computer wins!")
        losses += 1

print(f"\nFinal Score — You: {wins} | Computer: {losses} | Draws: {draws}")
