# import random
#
#
# def rockPaperScissor():
#     computerCounter = 0
#     humanCounter = 0
#     while computerCounter + humanCounter < 5:
#         computerChoice = random.choice(["rock", "paper", "scissor"])
#         humanChoice = input("Choose rock, paper or scissor: ").lower()
#
#         if computerChoice == humanChoice:
#             print("It's a tie!")
#         elif (computerChoice == "rock" and humanChoice == "scissor") or \
#                 (computerChoice == "paper" and humanChoice == "rock") or \
#                 (computerChoice == "scissor" and humanChoice == "paper"):
#             computerCounter += 1
#             print(f"Computer Wins! It has {computerCounter} wins.")
#         else:
#             humanCounter += 1
#             print(f"Human Wins! You have {humanCounter} wins.")
#     if computerCounter > humanCounter:
#         print("Computer Wins!")
#     else:
#         print("Human Wins!")
#
#     return "Game is Over"
#
#
# print(rockPaperScissor())



import random

def rockPaperScissor():
    humanCount = 0
    computerCount = 0
    while humanCount + computerCount <= 5:
        computer = random.choice(["rock", "paper", "scissor"])
        human = input("Enter your choice: ").lower()
        if computer == human:
            humanCount += 1
            computerCount += 1
            print("It's a tie!")
            print(f"Both of you did {computer}")
        elif (computer == "rock" and human == "scissor") or \
                (computer == "paper" and human == "rock") or \
                (computer == "scissor" and human == "paper"):
            computerCount += 1
            print("Computer got it!")
            print(f"You did {human} and Computer {computer}")
        else:
            humanCount += 1
            print("Human got it!")
            print(f"You did {human} and Computer {computer}")
    if humanCount > computerCount:
        print(f"Human won the game with {humanCount} wins")
    else:
        print(f"Computer won the game with {computerCount} wins")
    return "Game is Over"


print(rockPaperScissor())





















