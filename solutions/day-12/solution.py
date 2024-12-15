import numpy as np
from collections import defaultdict, deque

# Directions for moving in the grid (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Convert the input file to a grid of integers
def file_to_grid(filename):
    with open(filename, 'r') as input_file:
        # Read and convert the file to a grid.
        grid = [[char for char in line.strip()] for line in input_file]

    return grid


# A flood fill works for this but it needs modifying to accomdate for the perimiters.
def flood_fill_perimeter(grid, x, y, visited, plant_type):
    # Initialize the queue for BFS
    queue = deque([(x, y)])
    visited[x][y] = True
    area = 0
    perimeter = 0

    # Only exit the loop when the queue is empty.
    while queue:
        current_row, current_col = queue.popleft()
        area += 1

        # Explore the neighbouring cells as per the rules.
        for row_offset, col_offset in DIRECTIONS:
            neighbour_row = current_row + row_offset
            neighbour_col = current_col + col_offset

            # Check if the neighbour is within bounds.
            if 0 <= neighbour_row < len(grid) and 0 <= neighbour_col < len(grid[0]):
                # Ensure only unvisited cells of the same plant type are added to the queue.
                if not visited[neighbour_row][neighbour_col] and grid[neighbour_row][neighbour_col] == plant_type:
                    # Mark in the visited array.
                    visited[neighbour_row][neighbour_col] = True

                    # Queue the neighbour.
                    queue.append((neighbour_row, neighbour_col))

                # If not the plant type then add to the perimeter.
                elif grid[neighbour_row][neighbour_col] != plant_type:
                    perimeter += 1
            else:
                # If neighbour is out of bounds.
                perimeter += 1

    return area, perimeter    


# Solve part one using the flood_fill_perimeter function.
def part_one(grid):
    # Correct initialization of the visited grid to avoid shallow copying issues.
    visited = np.zeros((len(grid), len(grid[0])), dtype=bool)
    total_cost = 0
    
    # Create a dict to store the total cost for each plant type region
    region_costs = defaultdict(int)

    # Iterate through all the garden plots with the nested for loop.
    for row_index in range(len(grid)):
        for col_index in range(len(grid[0])):
            # Check if the plot has been visited. If not, flood fill.
            if not visited[row_index][col_index]:
                plant_type = grid[row_index][col_index]
                area, perimeter = flood_fill_perimeter(grid, row_index, col_index, visited, plant_type)

                # Calculate the cost for this region
                cost = area * perimeter

                # Add this cost to the region's total cost in the dict
                region_costs[plant_type] += cost

    # Sum up the costs of all regions
    total_cost = sum(region_costs.values())
    
    return total_cost


# This is an adaptation of the flood flow code used for part one, but for counting the sides.
def count_unique_sides(grid, x, y, visited, plant_type):
    # Initialize the queue for BFS
    queue = deque([(x, y)])
    visited.add((x, y))
    area = 0
    edges = set()
    
    # Only exit the loop when the queue is empty.
    while queue:
        current_row, current_col = queue.popleft()
        area += 1

        # Explore the neighboring cells in all four directions.
        for row_offset, col_offset in DIRECTIONS:
            neighbour_row = current_row + row_offset
            neighbour_col = current_col + col_offset
            direction = (row_offset, col_offset)
            
            # Check if the neighbor is within the grid bounds.
            if 0 <= neighbour_row < len(grid) and 0 <= neighbour_col < len(grid[0]):
                if grid[neighbour_row][neighbour_col] != plant_type:
                    # Add the edge if the neighbor is a different plant type
                    edges.add((current_row, current_col, row_offset, col_offset))
                if (neighbour_row, neighbour_col) not in visited and grid[neighbour_row][neighbour_col] == plant_type:
                    # Mark the neighbour as visited and add it to the queue.
                    visited.add((neighbour_row, neighbour_col))
                    queue.append((neighbour_row, neighbour_col))    
            else:
                # Add the edge if the neighbor is out of bounds
                edges.add((current_row, current_col, row_offset, col_offset))

    # Filter out duplicates to get unique edges
    edge_list = list(edges)
    unique_edges = set(edge_list)
    
    for edge in edge_list:
        current_row, current_col, row_offset, col_offset = edge
        # Check for horizontal duplicates.
        if (current_row, current_col - 1, row_offset, col_offset) in edges:
            unique_edges.discard((current_row, current_col - 1, row_offset, col_offset))
        # Repeat for vertical duplicates.
        if (current_row - 1, current_col, row_offset, col_offset) in edges:
            unique_edges.discard((current_row - 1, current_col, row_offset, col_offset))

    # Get the number of unique sides.
    sides = len(unique_edges)

    return area, sides


# Solve part two.
def part_two(grid):
    # Initialise the visited set and total cost.
    visited = set()
    total_cost = 0
    
    # Iterate through all the garden plots with the nested for loop
    for row_index in range(len(grid)):
        for col_index in range(len(grid[0])):
            # Checks whether the cell at the current row and column has already been visited.
            if (row_index, col_index) not in visited:
                plant_type = grid[row_index][col_index]
                area, sides = count_unique_sides(grid, row_index, col_index, visited, plant_type)
                cost = area * sides
                total_cost += cost

    return total_cost


# Convert the file to a grid.
grid = file_to_grid('input.txt')

print("Part One Answer {}".format(part_one(grid)))
print("Part Two Answer {}".format(part_two(grid)))

