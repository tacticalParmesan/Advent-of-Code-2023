"""
This is the first puzzle of Day 4 of the Advent of Code 2023 challenge.
The objective of the game is to find the winning numbers from the card
and counting the points, assured that every match after the first doubles
 the points.
More on https://adventofcode.com/2023/day/4
"""
import re
from pprint import pprint

# Opening the file and extracting the cards:
with (open('input.txt', mode ='r') as ipt):
    cards_to_parse = ipt.readlines()


# We will store the sum of the points inside the following variable
result: int = 0

# First of all we have to parse the input:
# a) Split the input into a dictionary that contains two list; winning nums and game nums:
# {"Card #": ([winning numbers], [game numbers])}
scratched_cards = {}
for card_to_parse in cards_to_parse:

    # Removing the escape now to avoid problems later
    card_to_parse = card_to_parse.replace("\n", " ")

    # Getting the Key "Card #" and removing it from the input
    if match := re.search(r"Card\s+\d+", card_to_parse):
        card_to_parse = card_to_parse.replace(f"{match.group(0)}:", "")

        # Getting the two lists of numbers and cleaning the input
        winning_n, game_n = card_to_parse.split("|")
        scratched_cards[match.group(0)] = (list(filter(lambda x: x != "", winning_n.split(" "))),
                                           list(filter(lambda x: x != "", game_n.split(" "))))


# Now that the input has been parsed it's time to check if our numbers are winning ones
for card in scratched_cards:
    print(scratched_cards[card])
    points = 0
    match = 0  # To check if this the first match or not
    # Accessing our numbers at index 1 of the numbers tuple store in the card key
    for number in scratched_cards[card][1]:
        # Check if our number is a winning one
        if number in scratched_cards[card][0]:
            print("Found winning number:", number)
            match += 1
            # Check for the number of matching number to correctly assign points
            if match > 1:
                points *= 2
            else:
                points += 1
    print("This card points:", points)
    print("__________________________")
    # Finally sum the points to the result
    result += points

print("Total points:", result)
