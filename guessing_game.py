"""
Python Web Development Techdegree
Project 1 - Number Guessing Game

"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("---- Welcome to the guessing game ----")

    num = random.randrange(1, 10)
    num_attempts = 0

    while True:
        try:
            user_input = int(input("Pick a number between 1 and 10: "))
            if not 0 < user_input <= 10:
                raise ValueError
            num_attempts += 1
            if user_input > num:
                print("It's lower")
            elif user_input < num:
                print("It's higher")
            else:
                print("You got it in {} attempts".format(num_attempts))
                play_again = input("Do you want to play again \n Type Y/y - Play Again: ")
                if play_again.lower() == "y":
                    num_attempts = 0
                else:
                    break
        except ValueError:
            print("Please enter valid number between 1 and 10")
    print("---- Hope you had fun playing the game. Keep playing and have fun!!! ----")


# Kick off the program by calling the start_game function.
start_game()
