#!/usr/bin/env python3

def split_into_two_lists(filename):
    with open(filename, 'r') as input_file:
        input_data = input_file.read()

        # Split the data into two parts based on the blank line
        pipe_values_part, comma_values_part = input_data.split("\n\n")

        # Process the x|y values into a 2D array and convert to integers
        pipe_values = [list(map(int, line.split('|'))) for line in pipe_values_part.splitlines()]

        # Process the comma separated values into a 2D array and convert to integers
        comma_values = [list(map(int, line.split(','))) for line in comma_values_part.splitlines()]

        return pipe_values, comma_values


def validate_update(update, rules):
    # Create a dictionary that maps each page number in the update to its index (position) in the list
    position = {page: i for i, page in enumerate(update)}

    # Iterate over each rule (x, y) in the rules list
    for x, y in rules:
        # Check if both x and y are present in the position dictionary
        # and if x appears after y in the update list
        if x in position and y in position and position[x] > position[y]:
            # If the rule is violated, return False
            return False

    # If none of the rules are violated, return True
    return True


def reorder_update(update, rules):
    # Loop until the validate function marks it as a valid row.
    while not validate_update(update, rules):
        for x, y in rules:
            if x in update and y in update:
                pos_x = update.index(x)
                pos_y = update.index(y)
                if pos_x > pos_y:
                    # Swap x and y to correct the order
                    update[pos_x], update[pos_y] = update[pos_y], update[pos_x]
    return update


# Split the input into two 2D arrays.
pipe_values, comma_values = split_into_two_lists('input.txt')

# For part one, get the correct updates.
correct_updates = [update for update in comma_values if validate_update(update, pipe_values)]

# Get the sum of the middle pages.
middle_pages_sum_correct = sum(update[len(update) // 2] for update in correct_updates)
print("Part One Answer: {}".format(middle_pages_sum_correct))

# For part two, get the incorrect updates.
incorrect_updates = [update for update in comma_values if not validate_update(update, pipe_values)]

# Reorder the incorrect updates until they pass validation.
reordered_incorrect_updates = [reorder_update(update, pipe_values) for update in incorrect_updates]

# Get the sum of the middle pages of the reordered incorrect updates.
middle_pages_sum_incorrect = sum(update[len(update) // 2] for update in reordered_incorrect_updates)
print("Part Two Answer: {}".format(middle_pages_sum_incorrect))
