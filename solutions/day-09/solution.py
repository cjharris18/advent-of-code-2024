from collections import deque

def read_file(filename):
    # Read the file and return it.
    with open(filename, 'r') as file:
        return file.read()


def map_to_queue_and_dict(disk_map):
    # Initialize the variables needed.
    uncompressed_disk_map = []
    count = 0
    index_count = 0

    # Uncompress it to start.
    for num in disk_map:
        if not (count % 2 == 0):
            # Replace any free space with a '.' and add to the list
            uncompressed_disk_map.extend(['.'] * int(num))
        else:
            # Insert the index value, populated by its size, and add to the list
            uncompressed_disk_map.extend([str(index_count)] * int(num))
            index_count += 1
        count += 1

    # Convert the uncompressed disk map from a list to a deque structure.
    disk_deque = deque(uncompressed_disk_map)

    return disk_deque


def move_file_blocks(disk_deque):
    # Initialize two pointers: one at the start and one at the end
    start = 0
    end = len(disk_deque) - 1

    while start < end:
        if disk_deque[start] == '.':
            # Move the element from the end to the current start position
            while end > start and disk_deque[end] == '.':
                end -= 1
            if end > start:
                disk_deque[start] = disk_deque[end]
                # Replace the end position with None
                disk_deque[end] = None
                # Move the end pointer left
                end -= 1
        # Move the start pointer right
        start += 1

    # Ensure all remaining '.' are replaced with None
    for i in range(start, len(disk_deque)):
        if disk_deque[i] == '.':
            disk_deque[i] = None

    return disk_deque


def move_whole_files(disk_deque):
    # Initialize pos_file to the last index of disk_deque
    pos_file = len(disk_deque) - 1
    # Find the maximum file ID number in disk_deque
    id_num = max(int(x) for x in disk_deque if x != '.')

    while id_num >= 0:
        # Move pos_file back to find the last occurrence of the current file ID
        while 0 < pos_file and disk_deque[pos_file] != str(id_num):
            pos_file -= 1
        if pos_file == 0:
            break

        # Determine the size of the current file
        pos_temp = pos_file
        while pos_temp >= 0 and disk_deque[pos_temp] == str(id_num):
            pos_temp -= 1
        file_size = pos_file - pos_temp

        # Initialize variables to track the start and length of free space
        free_space_start = -1
        free_space_length = 0

        # Iterate through the deque to find a suitable free space block
        for suitable_space in range(pos_file - file_size + 1):
            if disk_deque[suitable_space] == '.':
                # If we find a free space and haven't started tracking a block, set the start
                if free_space_start == -1:
                    free_space_start = suitable_space
                # Increment the length of the current free space block
                free_space_length += 1
                # If the current free space block is large enough, break the loop
                if free_space_length == file_size:
                    break
            else:
                # If we encounter a non-free space, reset the tracking variables
                free_space_start = -1
                free_space_length = 0

        # Move the file if a suitable span is found.
        if free_space_length == file_size:
            # Loop through the file size.
            for file in range(file_size):
                # Swap elements for each iteration.
                disk_deque[free_space_start + file], disk_deque[pos_file - file] = disk_deque[pos_file - file], '.'

        # Update pos_file and id_num for the next iteration
        pos_file -= file_size
        id_num -= 1

    # Replace all remaining '.' with None
    for index in range(len(disk_deque)):
        if disk_deque[index] == '.':
            disk_deque[index] = None

    return disk_deque


def calculate_checksum(dq):
    # Let's initialise the checksum.
    checksum = 0

    # Loop through each element in dq with its index.
    for position, block in enumerate(dq):
        if block != None:
            checksum += position * int(block)
    return checksum


def solve_part_one(disk_map):
    # Let's reverse the compression.
    disk_deque = map_to_queue_and_dict(disk_map)

    # Now that we have it uncompressed and in a deque structure, lets free up the space.
    final_deque = move_file_blocks(disk_deque)

    # Calculate the final checksum.
    checksum = calculate_checksum(final_deque)

    return checksum


def solve_part_two(disk_map):
    # Let's reverse the compression.
    disk_deque = map_to_queue_and_dict(disk_map)

    # Now that we have it uncompressed and in a deque structure, lets free up the space.
    final_deque = move_whole_files(disk_deque)

    # Calculate the final checksum.
    checksum = calculate_checksum(final_deque)

    return checksum


# Read the grid from the file
disk_map = read_file('input.txt')

part_one_answer = solve_part_one(disk_map)
print("Part One Answer {}".format(part_one_answer))

part_two_answer = solve_part_two(disk_map)
print("Part Two Answer {}".format(part_two_answer))