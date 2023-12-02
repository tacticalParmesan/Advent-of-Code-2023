"""
This is the second puzzle of Day 2 of the Advent of Code 2023 challenge.
The objective of the game is to find the fewest number of cubes of each color
to make the game possible and then retun the result of the multiplication
of those.
More on https://adventofcode.com/2023/day/2
"""
import re

# Opening the file and extracting the game log:
with open('input.txt', mode ='r') as ipt:
    games = ipt.readlines()

# We will store the power of the games inside the following variable according to
# the elf definition
power: int = 0

# To check if a game was possible we have to match the result of each draw with our dictionary
# First of all, let's iterate over the game input lines
for game in games:

    # Split the game draws into individual values
    draws = re.findall(r"\d\d? \w*", game)
    print(draws)

    # Unpack every number-color couple and store them into a dictionary
    # that accounts for the fewest number
    cubes = {'red': 0, 'blue': 0, 'green': 0}
    for draw in draws:
        num, color = draw.split()
        hand = {color: int(num)}
        if cubes[color] < hand[color]:
            cubes[color] = hand[color]


    # Add the power of each game to the result
    power += cubes['red'] * cubes['blue'] * cubes['green']

# Finally print the result
print(power)






