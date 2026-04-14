import random
def lepeshka():
    choices = ["rock", "paper", "scissors"]
    user = input("Enter rock, paper, or scissors: ").lower()
    computer = random.choice(choices)
    print("You chose:", user)
    print("Computer chose:", computer)
    if user == computer:
        print("It's a draw!")
    elif user not in choices:
        print("Incorrect input. Try again.")
    elif (user == "rock" and computer == "scissors") or  (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
while True:
    lepeshka()
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing!")
        break
