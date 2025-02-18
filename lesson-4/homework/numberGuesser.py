import random


def guessGame(number):
    i = 1
    randomNumber = random.randint(1, 100)
    max_trials = 10

    while i <= max_trials:
        if number == randomNumber:
            print("You guessed the number!")
            break
        elif number > randomNumber:
            print("Too high!")
        elif number < randomNumber:
            print("Too low!")

        if i < max_trials:
            print(f"You have {max_trials - i} trials left.")

        while True:
            try:
                number = int(input("Guess a number between 1 and 100: "))
                if number < 1 or number > 100:
                    print("Please enter a number between 1 and 100.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        i += 1

    if number != randomNumber:
        print(f"Sorry, you've run out of trials. The correct number was {randomNumber}.")


number = int(input("Guess a number between 1 and 100: "))
guessGame(number)
