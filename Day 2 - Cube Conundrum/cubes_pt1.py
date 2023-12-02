"""
This is the first puzzle of Day 2 of the Advent of Code 2023 challenge.
The objective of the game is to find which games in the input file are possible
given that inside a bag of cube there are only 12 red cubes,  13 green cubes,
and 14 blue cubes.
More on https://adventofcode.com/2023/day/2
"""
import re

# Storing the content of the bag as a dictionary constant
BAG = {"red": 12, "green": 13, "blue": 14}

# Opening the file and extracting the game log:
with open('input.txt', mode ='r') as ipt:
    games = ipt.readlines()

# We will store the sum of the *possible* games inside the following variable
result: int = 0

# To check if a game was possible we have to match the result of each draw with our dictionary
# First of all, let's iterate over the game input lines
for game in games:

    # The boolean check of this game's possibility
    is_possible: bool = True

    # Then we have to do a list of sub quests:
    # A) Save the game ID as an integer number:
    if match := re.search(r"\d\d?\d?:", game):
        game_id: int = int(match.group(0).replace(":", ""))

    # B) Split the game draws into individual values
    draws = re.findall(r"\d\d? \w*", game)
    print(draws)

    # C) Unpack every number-color couple and store into a dictionary
    for draw in draws:
        num, color = draw.split()
        cubes = {color: int(num)}
        print(cubes)

        # D) Compare the cubes in the hand with the ones in the bag
        for cube in cubes:
            if cubes[cube] > BAG[cube]:
                is_possible = False

    # If the above check didn't find more cubes than allowed than is_possible
    # should still be True, but if it didn't...
    if is_possible:
        # This means that we can add this game's id to the end result
        result += game_id

# Finally print the result
print(result)






