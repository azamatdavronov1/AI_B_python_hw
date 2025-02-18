import random


def rockPaperScissor():
    computerCounter = 0
    humanCounter = 0
    while computerCounter + humanCounter < 5:
        computerChoice = random.choice(["rock", "paper", "scissor"])
        humanChoice = input("Choose rock, paper or scissor: ").lower()

        if computerChoice == humanChoice:
            print("It's a tie!")
        elif (computerChoice == "rock" and humanChoice == "scissor") or \
                (computerChoice == "paper" and humanChoice == "rock") or \
                (computerChoice == "scissor" and humanChoice == "paper"):
            computerCounter += 1
            print(f"Computer Wins! It has {computerCounter} wins.")
        else:
            humanCounter += 1
            print(f"Human Wins! You have {humanCounter} wins.")
    if computerCounter > humanCounter:
        print("Computer Wins!")
    else:
        print("Human Wins!")

    return "Game is Over"


print(rockPaperScissor())
