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
# numbers for every single line.

# Opening the file and extracting the document:
with open('input.txt', mode ='r') as doc:
    calibration = doc.readlines()

# The final number to return
result: int = 0

# Iterate over every single line of the calibration document:
for line in calibration:
    nums_in_line = []  # List to store the new-found numbers

    # Iterate over every single character of the line to look for digits
    for char in line:
        if char.isdigit():

            # Append to the list the numbers found inside
            nums_in_line.append(char)

    # Concatenate the first and last digit from every line and...
    first_last = f"{nums_in_line[0]}{nums_in_line[-1]}"

    # ...convert them into an int and add them up to the result
    result += int(first_last)

print(result)
