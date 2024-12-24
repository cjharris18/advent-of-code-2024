#!/usr/bin/env python3
import math

# Define the width and height as global variables.
WIDTH = 101
HEIGHT = 103

# Function to read data from a file and parse it into a list of dictionaries
def read_from_file(filename):
    with open(filename, 'r') as input_file:
        data = input_file.read().strip().split('\n')
        # Create a dictionary, with a tuple for storing the values.
        return [{'p': tuple(map(int, entry.split(' v=')[0].strip('p=').split(','))),
                 'v': tuple(map(int, entry.split(' v=')[1].split(',')))} for entry in data if entry]

# Function to update the positions of robots based on their velocities
def update_positions(robots):
    for robot in robots:
        # Calculate the new x-coordinate by adding the velocity to the current position and taking modulo WIDTH
        new_x = (robot['p'][0] + robot['v'][0]) % WIDTH
        # Calculate the new y-coordinate by adding the velocity to the current position and taking modulo HEIGHT
        new_y = (robot['p'][1] + robot['v'][1]) % HEIGHT
        # Update the robot's position with the new coordinates
        robot['p'] = (new_x, new_y)

# Function to calculate the number of robots in each quadrant
def calculate_quadrant_counts(entries):
    # Lets initialise each quadrant as 0.
    quadrant_counts = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0}

    for robot in entries:
        # take the x and y of the p values.
        x, y = robot['p']
        # This discounts all in the middle cross.
        if x == WIDTH // 2 or y == HEIGHT // 2:
            continue
        elif x > WIDTH // 2 and y < HEIGHT // 2:
            quadrant_counts['Q1'] += 1
        elif x < WIDTH // 2 and y < HEIGHT // 2:
            quadrant_counts['Q2'] += 1
        elif x < WIDTH // 2 and y > HEIGHT // 2:
            quadrant_counts['Q3'] += 1
        elif x > WIDTH // 2 and y > HEIGHT // 2:
            quadrant_counts['Q4'] += 1

    return quadrant_counts

# Function to simulate the movement of robots for a given number of seconds and calculate the safety product
def part_one(entries):
    seconds = 100
    for second in range(seconds):
        update_positions(entries)
    quadrant_counts = calculate_quadrant_counts(entries)
    safety_product = math.prod(quadrant_counts.values())

    return safety_product

# Function to create a grid representation of the robots' positions
def create_grid(robots):
    # Create the grid, with . for empty spaces.
    grid = [["." for row in range(WIDTH)] for col in range(HEIGHT)]
    for robot in robots:
        x, y = robot['p']
        # populate the position of a robot with a 1.
        grid[y][x] = "1"
    return grid

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(''.join(str(cell) for cell in row))

# Function to find the tree shape in the grid
def find_tree_shape(grid):
    # Define the shape of the tree to find, this was taken off other reddit solutions for searching.
    tree_shape = [
        "1111111111111111111111111111111",
        "1                             1",
        "1                             1",
        "1                             1",
        "1                             1",
        "1              1              1",
        "1             111             1",
        "1            11111            1",
        "1           1111111           1",
        "1          111111111          1",
        "1            11111            1",
        "1           1111111           1",
        "1          111111111          1",
        "1         11111111111         1",
        "1        1111111111111        1",
        "1          111111111          1",
        "1         11111111111         1",
        "1        1111111111111        1",
        "1       111111111111111       1",
        "1      11111111111111111      1",
        "1        1111111111111        1",
        "1       111111111111111       1",
        "1      11111111111111111      1",
        "1     1111111111111111111     1",
        "1    111111111111111111111    1",
        "1             111             1",
        "1             111             1",
        "1             111             1",
        "1                             1",
        "1                             1",
        "1                             1",
        "1                             1",
        "1111111111111111111111111111111"
    ]

    # Get the width/height of the tree.
    tree_height = len(tree_shape)
    tree_width = len(tree_shape[0])

    # Loop through each possible starting position in the grid where the tree shape could fit
    for y in range(len(grid) - tree_height + 1):
        for x in range(len(grid[0]) - tree_width + 1):
            match = True  # Assume a match until proven otherwise
            # Loop through each cell in the tree shape
            for dy in range(tree_height):
                for dx in range(tree_width):
                    # Skip spaces in the tree shape
                    if tree_shape[dy][dx] == ' ':
                        continue
                    # If the grid cell does not match the tree shape cell, set match to False
                    if grid[y + dy][x + dx] != tree_shape[dy][dx]:
                        match = False
                        break  # Exit the inner loop early if a mismatch is found
                if not match:
                    break  # Exit the outer loop early if a mismatch is found
            if match:
                return (x, y)  # Return the position if a match is found

    return None  # Return None if no match is found

# Function to simulate the movement of robots and find the tree shape in the grid
def part_two(entries):
    # Try the first 10,000 seconds.
    for second in range(1, 10_000):
        update_positions(entries)
        grid = create_grid(entries)
        position = find_tree_shape(grid)
        if position:
            print(f"Tree shape found at second {second}")
            print_grid(grid)
            break


# Read data from 'input.txt' file
entries = read_from_file('input.txt')

print(f"Part One Answer: {part_one(entries)}")

# Read data from 'input.txt' file
p2_entries = read_from_file('input.txt')

part_two(p2_entries)
