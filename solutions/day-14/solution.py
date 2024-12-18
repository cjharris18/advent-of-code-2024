#!/usr/bin/env python3
import math

def read_from_file(filename):
    with open(filename, 'r') as input_file:
        data = input_file.read().strip().split('\n')
        return [{'p': tuple(map(int, entry.split(' v=')[0].strip('p=').split(','))),
                 'v': tuple(map(int, entry.split(' v=')[1].split(',')))} for entry in data if entry]

# Function to update the position of the robots with teleportation
def update_positions(robots, width, height):
    for robot in robots:
        new_x = (robot['p'][0] + robot['v'][0]) % width
        new_y = (robot['p'][1] + robot['v'][1]) % height
        robot['p'] = (new_x, new_y)

# Function to calculate the number of robots in each quadrant
def calculate_quadrant_counts(entries, width, height):
    quadrant_counts = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0}

    for robot in entries:
        x, y = robot['p']
        if x == width // 2 or y == height // 2:
            continue
        elif x > width // 2 and y < height // 2:
            quadrant_counts['Q1'] += 1
        elif x < width // 2 and y < height // 2:
            quadrant_counts['Q2'] += 1
        elif x < width // 2 and y > height // 2:
            quadrant_counts['Q3'] += 1
        elif x > width // 2 and y > height // 2:
            quadrant_counts['Q4'] += 1

    return quadrant_counts

def part_one(entries):
    # Define the dimensions of the grid
    width = 101
    height = 103

    # Update the positions of the robots for 100 seconds
    for _ in range(100):
        update_positions(entries, width, height)

    # Calculate the number of robots in each quadrant
    quadrant_counts = calculate_quadrant_counts(entries, width, height)

    # Multiply the safety values together
    safety_product = math.prod(quadrant_counts.values())

    return safety_product


# Read data from 'input.txt' file
entries = read_from_file('input.txt')

print(f"Part One Answer: {part_one(entries)}")
