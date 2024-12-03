#!/usr/bin/env python3

import re


def part_one():
    # Initialise input_data as global.
    global input_data

    # Set the calc variable at zero.
    total_sum = 0

    # Set the regex pattern.
    pattern = r"mul\([0-9]+,[0-9]+\)"

    # Get a list of all the matches.
    matches = re.findall(pattern, input_data)

    for match in matches:
        # Separate mal(x,y) into x and y.
        num_1, num_2 = map(int, match.strip('mul()').split(','))
        total_sum += num_1 * num_2

    print("Part One Answer: {}".format(total_sum))


def part_two():
    # Initialise input_data as global.
    global input_data

    # Set the calc variable as 0.
    total_sum = 0

    # Let's create a modified pattern to get the do's and don'ts
    pattern_modified = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"

    unfiltered = re.findall(pattern_modified, input_data)

    # Let's set a state edited by the Do's and Don'ts.
    state = True

    for match in unfiltered:
        if match == "do()":
            state = True
        elif match == "don't()":
            state = False
        elif state:
            # Separate mal(x,y) into x and y.
            num_1, num_2 = map(int, match.strip('mul()').split(','))
            total_sum += num_1 * num_2

    print("Part Two Answer: {}".format(total_sum))


# Let's read the data from the file.
with open('input.txt', 'r') as file:
    input_data = file.read()

    # Solve the first part.
    part_one()

    # Solve the second part.
    part_two()