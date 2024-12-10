#!/usr/bin/env python3
from collections import deque

# A breadth first search algorithm that utilises the deque structure.
def bfs(grid, start_position):
    queue = deque([start_position])  # Initialize the queue with the starting position
    visited_positions = {start_position}  # Initialize the visited set with the starting position
    trailhead_score = 0  # Initialize the score for the current trailhead

    while queue:
        current_x, current_y = queue.popleft()  # Dequeue the current position

        # Explore all possible moves (up, down, left, right)
        for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = current_x + delta_x, current_y + delta_y  # Calculate the new position
            # Check if the new position is within bounds, not visited, and height increases by 1
            if (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and
                    (new_x, new_y) not in visited_positions and grid[new_x][new_y] == grid[current_x][current_y] + 1):
                queue.append((new_x, new_y))  # Enqueue the new position
                visited_positions.add((new_x, new_y))  # Mark the new position as visited
                if grid[new_x][new_y] == 9:  # If the new position has height 9, increment the score
                    trailhead_score += 1

    return trailhead_score

def bfs_part_two(grid, start_position):  # for part two, some changes are needed.
    queue = deque([[start_position]])  # Initialize the queue with the starting position as a path
    distinct_paths_count = 0  # Initialize the count of distinct paths

    while queue:
        path = queue.popleft()  # Dequeue the current path
        current_x, current_y = path[-1]  # Get the current position from the end of the path

        # Explore all possible moves (up, down, left, right)
        for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = current_x + delta_x, current_y + delta_y  # Calculate the new position
            if (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and
                    (new_x, new_y) not in path and grid[new_x][new_y] == grid[current_x][current_y] + 1):
                new_path = path + [(new_x, new_y)]  # Create a new path with the new position
                if grid[new_x][new_y] == 9:  # If the new position has height 9, increment the count
                    distinct_paths_count += 1
                else:
                    queue.append(new_path)  # Enqueue the new path

    return distinct_paths_count  # Return the count of distinct paths

def part_two(grid):
    total_rating = 0  # Initialize the total rating
    for x in range(len(grid)):  # Iterate over all positions in the grid
        for y in range(len(grid[0])):
            if grid[x][y] == 0:  # If the position is a trailhead (height 0)
                total_rating += bfs_part_two(grid, (x, y))  # Add the count of distinct paths to the total rating
    return total_rating  # Return the total rating

def part_one(grid):
    total_score = 0  # Initialize the total score
    for x in range(len(grid)):  # Iterate over all positions in the grid
        for y in range(len(grid[0])):
            if grid[x][y] == 0:  # If the position is a trailhead (height 0)
                total_score += bfs(grid, (x, y))  # Add the score from BFS to the total score
    return total_score

# Convert the input file to a grid of integers
def file_to_grid(filename):
    with open(filename, 'r') as input_file:
        # Read and convert each line to a list of integers
        grid = [[int(digit) for digit in line.strip()] for line in input_file]

    return grid


# Read the grid from the input file
grid = file_to_grid('input.txt')

# Print the total score for all trailheads
part_one_answer = part_one(grid)  # This should print the total score for all trailheads
print("Part One Answer: {}".format(part_one_answer))

part_two_answer = part_two(grid)
print("Part Two Answer: {}".format(part_two_answer))