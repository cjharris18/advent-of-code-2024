#!/usr/bin/env python3

def create_lists_from_file(file_name):
    # Read the file
    with open(file_name, 'r') as file:
        # Use list comprehensions to create the two lists.
        # 1. the line.strip() is error handling for blank lines (this proved necessary for some reason).
        # 2. Split each line into numbers and convert them to integers using `map(int, ...)`.
        # 3. Use zip with unpacking (*) to group first and second numbers separately.
        list_1, list_2 = zip(*(map(int, line.split()) for line in file if line.strip()))

    # Convert the tuples back to lists as zip returns tuples.
    return list(list_1), list(list_2)

def part_one(list_1, list_2):
    return sorted(list_1), sorted(list_2)

def part_two(left_list, right_list):
    # 1. the zip part creates pairs from the two lists.
    # 2. the abs part calculates the absolute difference for each pair.
    # Absolute values are used to measure the magnitude of the difference between two values, not if one is larger or smaller.
    # 3. the sum adds up all these differences to get the total distance.
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))

    return total_distance

# Create the lists from the provided input.
list_1, list_2 = create_lists_from_file('input.txt')

# Sort the lists into ascending order.
list_1_asc, list_2_asc = part_one(list_1, list_2)

# Return the answer for the solution by using the part two function.
answer = part_two(list_1_asc, list_2_asc)

print("Day 1 Answer: {}".format(answer))