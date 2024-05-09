import random

min_value = 1
max_value = 100

def num_guess():
    return random.randint(min_value, max_value)

def play_game():
    target_number = num_guess()
    while True:
        guess = input(f"I am thinking of a number between {min_value} and {max_value}. \nCan you guess what number I am thinking of?  ")
        if guess.isdigit():
            guess =int(guess)
            if min_value <= guess <= max_value:
                if guess < target_number:
                    print("Too low, try again.")
                elif guess > target_number:
                    print("Too high, try again,")
                else:
                    print(f"You guessed correctly! The number I was thinking of was: {target_number}")
                    break
        else:
            print("Invalid input. Please enter a number between 1 and 100.")

        replay = input("You did not guess correctly. Would you like to try again? (y/n) ")
        if replay.lower() != "y":
            break
        else:
            print("Thanks for playing!")

play_game()

