# Part 2 requires to convert digits that are spelled with letters:
# use word_to_number and regex
import re
from word2number import w2n

"""
We are about to get launched into the sky to save Christmas or something?
Well, seems like that we are even obliged to help the elves to fire our
nerdy ass into space, let's help them with deciphering the calibration docs.
"""

"""
This is the first puzzle of Day 1 of the Advent of Code 2023 challenge.
"""

# I save the input text for the calibration document into a .txt file
# since we have to get the sum of every couple of first and last concatenated
# numbers (env if spelled out as words) for every single line.

# Opening the file and extracting the document:
with open('input.txt', mode='r') as doc:
    calibration = doc.readlines()

# The final number to return
result: int = 0

# Iterate over every single line of the calibration document:
for line in calibration:

    # Search for a number, either as a digits or as a word
    # BEWARE OF OVERLAPPING EXPRESSIONS!
    if matches := re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line):

        # Convert all the word numbers into digits
        for i in range(len(matches)):
            if not matches[i].isdigit():
                matches[i] = w2n.word_to_num(matches[i])

            # Convert all to integers
            matches[i] = int(matches[i])

    # Concatenate the first and last digit from every line and...
    first_last: str = f"{matches[0]}{matches[-1]}"

    # ...convert them into an int and add them up to the result
    result += int(first_last)

print(result)
