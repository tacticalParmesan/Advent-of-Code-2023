"""
This is the first puzzle of Day 3 of the Advent of Code 2023 challenge.
The objective of the game is to find the missing part of the engine of the
gondola lift that will bring you to the water source.
More on https://adventofcode.com/2023/day/3
"""
# We will store the sum of the *possible* parts inside the following variable
result: int = 0

# Opening the file and extracting the engine schematic
with open('input.txt', mode ='r') as ipt:
    parts = ipt.readlines()
    scheme = [list(part) for part in parts]

# The list of symbols minus the dot and the escape: obtained separately with a nested loop
SYMBOLS = ['=', '&', '+', '-', '@', '*', '%', '#', '/', '$']

# Since a number is a part number only when adjacent to a symbol
# let's define some values for the position of the number and a
# 'capturing matrix' to search for a symbol.
pos = [0,0]

# Let's find all symbols and store their surrounding coordinates in a list
valid_positions = []
for row in range(len(scheme)):
    for col in range(len(scheme[row])):

        # Look for a symbol
        search = scheme[row][col]
        if search in SYMBOLS:
            
            # Set its position as the relative path of the matrix to store the positions of valid parts
            pos[0] = row
            pos[1] = col
            matrix = [(pos[0] - 1, pos[1] - 1),  # Upper row
                      (pos[0], pos[1] - 1),
                      (pos[0] + 1, pos[1] - 1),
                      (pos[0] - 1, pos[1]),  # Center row
                      (pos[0] + 1, pos[1]),
                      (pos[0] - 1, pos[1] + 1),  # Lower row
                      (pos[0], pos[1] + 1),
                      (pos[0] + 1, pos[1] + 1)]

            # Add every valid position to the list
            for m in matrix:
                valid_positions.append(m)

# Now it's time to look for numbers
full_num: str = ""  # To be converted to int and summed to the final output if checks are OK
num_pos = []  # A list of positions of the digits to check if we are near a symbol
for row in range(len(scheme)):
    for col in range(len(scheme[row])):

        # Get together a full number until we touch a dot, in that case reset the number to empty
        n = scheme[row][col]
        if n.isdigit():
            # We found a number, we store its position to check later if this is a valid part and the number itself
            full_num += n
            num_pos.append((row, col))

        else:
            # We found a dot or an escape character, so we now check for symbols and break out of the column loop
            # Just need to compare the tuples here
            for coord in num_pos:
                if coord in valid_positions:
                    # We found a part, add this number to the total and reset everything and keep on searching
                    try:
                        result += int(full_num)
                    except ValueError:
                        pass
                    full_num = ""
                    num_pos = []

            # If we didn't find anything, we will still reset our values
            full_num = ""
            num_pos = []

print(result)














