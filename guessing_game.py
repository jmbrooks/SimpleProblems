# -*- coding: utf-8 -*-
from random import randint
import msvcrt


def new_secret_number(lowest_digit: int=1, largest_digit: int=100) -> int:
    """Generate new random number."""
    return randint(lowest_digit, largest_digit)


def main():
    """Run guessing game application."""
    print("Time to play a guessing game.\n")
    secret_number = new_secret_number()
    guesses = 0

    while True:
        if guesses == 0:
            entry = int(input("Enter number between 1 & 100: ").strip().lower())

        if ((msvcrt.kbhit() and ord(msvcrt.getch()) == 27) or entry == 0):
            print("Ending game.")
            break
        elif entry > secret_number:
            guesses += 1
            entry = int(input('Too high. Try again: ').strip().lower())
        elif entry < secret_number:
            guesses += 1
            entry = int(input('Too low. Try again: ').strip().lower())
        elif entry == secret_number:
            guesses += 1
            print("Congratulations! You got it in {} guesses.".format(
            guesses
            ))
            continue_game = input("Play again?(Y/n):")
            if continue_game.strip().lower() in ['yes', 'y']:
                guesses = 0
                secret_number = new_secret_number()
            else:
                print("Ending game.")
                break


if __name__ == '__main__':
    main()
