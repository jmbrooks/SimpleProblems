# -*- coding: utf-8 -*-
from random import randint


def generate_numbers() -> list:
    """Generates winning Powerball numbers as list."""
    powerball_numbers = []
    for i in range(5):
        powerball_numbers.append(randint(1, 53))
    powerball_numbers.append(randint(1, 42))
    return powerball_numbers


def play_powerball():
    """Plays the Powerball game."""
    print("Official, fruitless, Powerball number generator.")
    games_to_play = int(input("How many sets of numbers? ").strip().lower())

    winning_numbers = generate_numbers()
    print("Winning Numbers: {}".format(winning_numbers))

    for number in range(games_to_play):
        my_numbers = generate_numbers()
        matches = [i for i, j in zip(my_numbers, winning_numbers) if i == j]

        if len(matches) >= 4:
            print("Game: {}. Your numbers:\t{}\t{}\t{}\t{}\t{}\t"
            "Powerball: {}\tMatches: {}".format(
                number, my_numbers[0], my_numbers[1], my_numbers[2],
                my_numbers[3], my_numbers[4], my_numbers[5], len(matches)
            ))


if __name__ == '__main__':
    play_powerball()
