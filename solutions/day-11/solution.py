#!/usr/bin/env python3
from functools import cache

def read_file(filename):
    with open(filename, 'r') as input_file:
        return [int(n) for n in input_file.read().strip().split()]

def blink(number):
    # If the stone is 0, return 1 as per the first rule.
    if number == 0:
        return [1]

    # Get the length of the digits.
    len_digits = len(str(number))

    # Logic for when the number of digits is even.
    if len_digits % 2 == 0:
        mid = len_digits // 2
        left = int(str(number)[:mid])
        right = int(str(number)[mid:])
        result = [left, right]
        return result

    # the final rule for when none of the other conditions are met.
    return [number * 2024]

@cache  # this automatically caches the results. Helping with efficiency for part two.
def count_the_splits(number, blinks):
    # Ensure correct recursion termination.
    if blinks == 0:
        return 1

    # Iterate through the number of blinks provided.
    result = 0
    for num in blink(number):
        result += count_the_splits(num, blinks - 1)
    return result

def solve(numbers, num_of_splits):
    stones = 0
    for num in numbers:
        # Iterate through our list, and count the number of splits for the number and the provided number to split.
        stones += count_the_splits(num, num_of_splits)
    return stones


# Read numbers from the input file.
numbers = read_file('input.txt')

# Calculate the result for the actual input.
part_one_answer = solve(numbers, 25)
print("Part One Answer: {}".format(part_one_answer))

part_two_answer = solve(numbers, 75)
print("Part Two Answer: {}".format(part_two_answer))
