from collections import defaultdict
import itertools


def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        grid = [list(line.strip()) for line in lines]
        return grid


def get_map_and_nodes(grid):
    map_data = {}
    nodes = defaultdict(list)
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            map_data[(y, x)] = char
            if char != '.':
                nodes[char].append((y, x))
    return map_data, nodes


def calculate_first_antinodes(antenna1, antenna2):
    delta_y, delta_x = antenna2[0] - antenna1[0], antenna2[1] - antenna1[1]
    return (antenna1[0] - delta_y, antenna1[1] - delta_x), (antenna2[0] + delta_y, antenna2[1] + delta_x)


def calculate_all_antinodes(antenna1, antenna2):
    delta_y, delta_x = antenna2[0] - antenna1[0], antenna2[1] - antenna1[1]
    for i in itertools.count():
        yield {(antenna1[0] - delta_y * i, antenna1[1] - delta_x * i),
               (antenna2[0] + delta_y * i, antenna2[1] + delta_x * i)}


def find_first_antinodes(map_data, nodes):
    seen_antinodes = set()
    for node_set in nodes.values():
        for pair in itertools.combinations(node_set, r=2):
            antinodes = calculate_first_antinodes(*pair)
            seen_antinodes.update({antinode for antinode in antinodes if antinode in map_data})
    return seen_antinodes


def find_all_antinodes(map_data, nodes):
    seen_antinodes = set()
    for node_set in nodes.values():
        for pair in itertools.combinations(node_set, r=2):
            for antinodes in calculate_all_antinodes(*pair):
                valid_antinodes = map_data.keys() & antinodes
                if not valid_antinodes:
                    break
                seen_antinodes.update(valid_antinodes)
    return seen_antinodes


def part_one(grid):
    map_data, nodes = get_map_and_nodes(grid)
    return len(find_first_antinodes(map_data, nodes))


def part_two(grid):
    map_data, nodes = get_map_and_nodes(grid)

    # Find all antinodes
    all_antinodes = find_all_antinodes(map_data, nodes)

    # Include the positions of each antenna (unless that antenna is the only one of its frequency)
    for node_set in nodes.values():
        if len(node_set) > 1:
            all_antinodes.update(node_set)

    return len(all_antinodes)


# Read the grid from the file
grid = read_grid_from_file('input.txt')

# Call the main function to solve the problem
part_one_answer = part_one(grid)
part_two_answer = part_two(grid)

# Print the results
print("Part One Answer {}".format(part_one_answer))
print("Part Two Answer {}".format(part_two_answer))