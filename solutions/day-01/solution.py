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


def part_one(left_list, right_list):
    # 1. the zip part creates pairs from the two lists.
    # 2. the abs part calculates the absolute difference for each pair.
    # Absolute values are used to measure the magnitude of the difference between two values, not if one is larger or
    # smaller.
    # 3. the sum adds up all these differences to get the total distance.
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))

    print("Part One Answer: {}".format(total_distance))


def part_two(left_list, right_list):
    # Define the similarity score.
    similarity_score = 0
    # Cache to store previously computed scores
    cache = {}

    # Let's cycle through both for loops.
    for num_left in left_list:
        if num_left in cache:
            similarity_score += cache[num_left]
        else:
            count = 0
            for num_right in right_list:
                if num_right > num_left:
                    break
                if num_left == num_right:
                    count += 1

            score = num_left * count
            cache[num_left] = score
            similarity_score += score

    print("Part Two Answer: {}".format(similarity_score))

# Create the lists from the provided input.
list_1, list_2 = create_lists_from_file('input.txt')

# Solve part one and sort the lists.
part_one(sorted(list_1), sorted(list_2))

# Solve part two and sort the lists.
part_two(sorted(list_1), sorted(list_2))
