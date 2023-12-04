"""
This is the first puzzle of Day 3 of the Advent of Code 2023 challenge.
The objective of the game is to find the missing part of the engine of the
gondola lift that will bring you to the water source.
More on https://adventofcode.com/2023/day/3
"""
import re
from pprint import pprint

# # We will store the sum of the *possible* parts inside the following variable
result: int = 0

# Opening the file and extracting the engine schematic
with open('input.txt', mode ='r') as ipt:
    parts = ipt.readlines()
    scheme = [list(part) for part in parts]
    pprint(scheme)

# The list of symbols minus the dot and the escape: obtained separately with a nested loop
symbols = ['=', '&', '+', '-', '@', '*', '%', '#', '/', '$']

# Since a number is a part number only when adjacent to a symbol
# let's define some values for the position of the number and a
# 'capturing matrix' to search for a symbol.
pos = {"x": 0, "y": 0}
matrix = [(pos['x'] - 1, pos['y'] - 1),  # Upper row
                      (pos['x'], pos['y'] - 1),
                      (pos['x'] + 1, pos['y'] - 1),
                      (pos['x'] - 1, pos['y']),  # Center row
                      (pos['x'] + 1, pos['y']),
                      (pos['x'] - 1, pos['y'] + 1),  # Lower row
                      (pos['x'], pos['y'] + 1),
                      (pos['x'] + 1, pos['y'] + 1)]

# Let's find all numbers and store them and their position in a list
numbers = []
for part in parts:
    if matches := re.search(r"\d\d?\d?", part):
        print(matches.string)
        print(matches.span())

    print(numbers)






