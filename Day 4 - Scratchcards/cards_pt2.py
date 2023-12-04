"""
This is the second puzzle of Day 4 of the Advent of Code 2023 challenge.
The objective of the game is to find the winning numbers from the card
and counting the points, assured that every match after the first doubles
the points. (Part 2:) You win (n == points) copies of the cards below the winning card;

More on https://adventofcode.com/2023/day/4
"""
import re

# Opening the file and extracting the cards:
with (open('input.txt', mode ='r') as ipt):
    cards_to_parse = ipt.readlines()

# We will store the sum of the total won cards inside the following variable
# starting with the original cards
result: int = 0

# First of all we have to parse the input:
# Split the input into a dictionary that contains two list; winning nums and game nums:
# {"Card #": ([winning numbers], [game numbers])}
original_cards = {}
for card_to_parse in cards_to_parse:

    # Removing the escape now to avoid problems later
    card_to_parse = card_to_parse.replace("\n", " ")

    # Getting the card number and removing it from the input
    if match := re.search(r"Card\s+\d+", card_to_parse):
        card_to_parse = card_to_parse.replace(f"{match.group(0)}:", "")

        # Getting the two lists of numbers and cleaning the input, the last is the number of instances
        winning_n, game_n = card_to_parse.split("|")
        original_cards[int(match.group(0).replace("Card ", ""))] = \
            [list(filter(lambda x: x != "", winning_n.split(" "))),
             list(filter(lambda x: x != "", game_n.split(" "))), 1]


# Now that the input has been parsed it's time to check if our numbers are winning ones
for card in original_cards:
    print(f"Current card: {original_cards[card]}: Copies: {original_cards[card][2]}")
    matches = 0  # To check if this the first match or not

    # Accessing our numbers at index 1 of the numbers tuple store in the card key
    for number in original_cards[card][1]:

        # Check if our number is a winning one
        if number in original_cards[card][0]:
            print("Found winning number:", number)
            matches += 1
    print("This card matches:", matches)

    # Add a copy to the (n == matches) cards times the copies of this very card
    for i in range(1, matches + 1):
        original_cards[card + i][2] += 1 * original_cards[card][2]
        print(f"Added {1 * original_cards[card][2]} copies to Card {card + i}")
    print("__________________________")
    
    # Finally sum the copies to the result
    result += original_cards[card][2]

print("Total cards:", result)
