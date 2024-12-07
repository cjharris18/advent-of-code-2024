import numpy as np

class Solution(object):
    def __init__(self):
        # To track visited positions during guard simulation
        self.visited = set()
        # Starting position of the guard
        self.start_position = None
        # To store the original path of the guard
        self.original_path = None

    def read_grid_from_file(self, filename):
        # Read the file and convert each line into a list of characters
        with open(filename, 'r') as file:
            lines = file.readlines()
            grid = [list(line.strip()) for line in lines]
        
        # Convert the grid to a numpy array
        board = np.array(grid)

        # Find the guard's starting position in the grid
        self.start_position = self.find_guard_start(board)

        return board

    def find_guard_start(self, board):
        # Search for the guard's starting symbol (^, >, v, <) in the grid
        for row in range(board.shape[0]):
            for col in range(board.shape[1]):
                if board[row][col] in {'^', '>', 'v', '<'}:
                    return (row, col)
        return None

    def simulate_guard(self, board):
        # Define the movement directions for each symbol
        directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
        # Define how the guard turns when blocked
        turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
        rows, cols = board.shape
        # Start from the guard's initial position and direction
        guard_pos = self.start_position
        guard_dir = board[guard_pos]

        # Clear any previously visited positions
        self.visited.clear()

        while True:
            row, col = guard_pos
            # Mark the current position as visited
            self.visited.add(guard_pos)
            delta_row, delta_col = directions[guard_dir]
            new_row, new_col = row + delta_row, col + delta_col

            # If the next position is within bounds and not an obstacle, move the guard
            if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] != '#':
                guard_pos = (new_row, new_col)
            else:
                # If there's an obstacle, turn the guard and update the board
                guard_dir = turns[guard_dir]
                board[row][col] = guard_dir

            # Stop if the guard moves out of bounds
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                break

        # Return the number of distinct positions visited
        return len(self.visited)

    def simulate_initial_guard_movement(self, board):
        directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
        turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
        rows, cols = board.shape
        guard_pos = self.start_position
        guard_dir = board[guard_pos]

        # Track the path taken by the guard
        path = []
        visited_states = set()

        while True:
            row, col = guard_pos
            # Track the current state (position and direction)
            state = (row, col, guard_dir)
            
            # Stop if this state was already visited (loop detected)
            if state in visited_states:
                break
            
            path.append(guard_pos)
            visited_states.add(state)
            self.visited.add(guard_pos)
            
            delta_row, delta_col = directions[guard_dir]
            new_row, new_col = row + delta_row, col + delta_col

            # Move the guard if the next position is valid
            if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] != '#':
                guard_pos = (new_row, new_col)
            else:
                # Turn the guard if blocked
                guard_dir = turns[guard_dir]
                board[row][col] = guard_dir

            # Stop if the guard moves out of bounds
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                break

        return path

    def identify_loop_points(self, path, board):
        directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
        rows, cols = board.shape
        potential_loop_points = set()

        # For each position in the guard's path, check adjacent cells
        for pos in path:
            row, col = pos
            for delta_row, delta_col in directions.values():
                test_row, test_col = row + delta_row, col + delta_col
                # If the adjacent cell is empty ('.'), it could be a valid obstruction point
                if 0 <= test_row < rows and 0 <= test_col < cols and board[test_row][test_col] == '.':
                    potential_loop_points.add((test_row, test_col))

        return potential_loop_points

    def test_obstruction_placement(self, board, position):
        # Create a copy of the board and place an obstruction ('#') at the given position
        test_board = np.copy(board)
        test_board[position[0]][position[1]] = '#'

        directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
        turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
        guard_pos = self.start_position
        guard_dir = board[guard_pos]

        visited_states = set()

        while True:
            state = (guard_pos, guard_dir)
            # If the state repeats, the guard is stuck in a loop
            if state in visited_states:
                return True
            visited_states.add(state)

            row, col = guard_pos
            delta_row, delta_col = directions[guard_dir]
            new_row, new_col = row + delta_row, col + delta_col

            # Move the guard if the next position is valid
            if 0 <= new_row < board.shape[0] and 0 <= new_col < board.shape[1] and test_board[new_row][new_col] != '#':
                guard_pos = (new_row, new_col)
            else:
                # Turn the guard if blocked
                guard_dir = turns[guard_dir]
                test_board[row][col] = guard_dir

            # Stop if the guard moves out of bounds
            if not (0 <= new_row < board.shape[0] and 0 <= new_col < board.shape[1]):
                break

        return False

    def count_valid_obstruction_positions(self, board):
        # Get the guard's original path
        self.original_path = self.simulate_initial_guard_movement(np.copy(board))

        # Identify potential loop points along the path
        loop_points = self.identify_loop_points(self.original_path, board)

        valid_positions = 0

        # Test each potential obstruction point to see if it causes a loop
        for position in loop_points:
            if self.test_obstruction_placement(np.copy(board), position):
                valid_positions += 1

        return valid_positions


# Read the grid from the file.
solution = Solution()
board = solution.read_grid_from_file('input.txt')

# Part One: Simulate the guard's movement and count the distinct positions visited
distinct_positions_test_case = solution.simulate_guard(np.copy(board))
print("Part One Answer: {}".format(distinct_positions_test_case))

# Part Two: Count valid obstruction positions
obstruction_positions = solution.count_valid_obstruction_positions(np.copy(board))
print("Part Two Answer: {}".format(obstruction_positions))
