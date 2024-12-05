import numpy as np

class Solution(object):
    def count_occurrences(self, board, word):
        # Get the number of rows (n) and columns (m) in the board
        n = len(board)
        m = len(board[0])
        count = 0
        # Iterate through each cell in the board
        for i in range(n):
            for j in range(m):
                # If the first character of the word matches the current cell
                if word[0] == board[i][j]:
                    # Start searching for the word from this cell
                    count += self.find_all(board, word, i, j)
        return count

    def find_all(self, board, word, row, col, i=0, direction=None):
        # If the entire word has been found, return 1
        if i == len(word):
            return 1
        # If out of bounds or current cell does not match the current character of the word, return 0
        if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0 or word[i] != board[row][col]:
            return 0

        # Temporarily mark the cell as visited by replacing its value with '*'
        temp = board[row][col]
        board[row][col] = '*'

        count = 0
        # Check all 8 possible directions if no direction is specified
        if direction is None or direction == 'down':
            count += self.find_all(board, word, row + 1, col, i + 1, 'down')
        if direction is None or direction == 'up':
            count += self.find_all(board, word, row - 1, col, i + 1, 'up')
        if direction is None or direction == 'right':
            count += self.find_all(board, word, row, col + 1, i + 1, 'right')
        if direction is None or direction == 'left':
            count += self.find_all(board, word, row, col - 1, i + 1, 'left')
        if direction is None or direction == 'down-right':
            count += self.find_all(board, word, row + 1, col + 1, i + 1, 'down-right')
        if direction is None or direction == 'up-left':
            count += self.find_all(board, word, row - 1, col - 1, i + 1, 'up-left')
        if direction is None or direction == 'down-left':
            count += self.find_all(board, word, row + 1, col - 1, i + 1, 'down-left')
        if direction is None or direction == 'up-right':
            count += self.find_all(board, word, row - 1, col + 1, i + 1, 'up-right')

        # Restore the cell's original value after searching in all directions
        board[row][col] = temp

        return count

    def count_xmas_patterns(self, data):
        rows, cols = len(data), len(data[0])
        count = 0

        _set = {"M", "S"}

        # Find 'A' as the center of the cross, then check the diagonals
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if data[r][c] == "A":
                    if {data[r - 1][c - 1], data[r + 1][c + 1]} == _set and {data[r - 1][c + 1], data[r + 1][c - 1]} == _set:
                        count += 1

        return count

def read_grid_from_file(filename):
    # Read the grid from a file and convert it to a list of lists (2D array)
    with open(filename,'r') as file:
        lines = file.readlines()
        grid = [list(line.strip()) for line in lines]
    return np.array(grid)

# Read the grid from the file
board = read_grid_from_file('input.txt')

word_search = Solution()

# Count and print the number of occurrences of "XMAS" in the grid (Part One)
print("Part One Answer: {}".format(word_search.count_occurrences(board,"XMAS")))

# Count and print the number of occurrences of "X-MAS" pattern in the grid (Part Two)
print("Part Two Answer: {}".format(word_search.count_xmas_patterns(board)))
