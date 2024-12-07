#!/usr/bin/env python3

# Function to read and parse input data from a file
def read_input(filename):
    with open(filename) as file:
        data = file.read().strip().split("\n")
    
    results = []  # List to store the test results (the number before the colon)
    terms = []  # List to store the numbers after the colon in each equation
    
    # Iterate through each line in the data
    for line in data:
        if line.strip():  # Skip empty lines
            result, *numbers = line.split(":")  # Split the line into result and numbers
            results.append(int(result))  # Convert the result to an integer and append it to the results list
            terms.append(list(map(int, numbers[0].split())))  # Convert numbers after the colon into a list of integers
    
    return results, terms  # Return the results and terms as two separate lists

# DFS function to explore possible operator combinations
def dfs(numbers, i, current_sum, result, operators):
    # If we've considered all numbers, check if the current sum matches the result
    if i == len(numbers):
        return current_sum == result
    else:
        next_number = numbers[i]  # Get the next number in the list
        
    # Define a dictionary that maps operators to their corresponding operations
    operations = {
        '+': lambda x, y: x + y,  # Addition operation
        '*': lambda x, y: x * y,  # Multiplication operation
        '||': lambda x, y: int(str(x) + str(y))  # Concatenation operation (combines digits as a string)
    }

    # Explore all operators and calculate the resulting options
    options = [operations[op](current_sum, next_number) for op in operators]  # Apply each operator to the current sum

    # Recur with all the resulting options and return true if any of them result in the correct answer
    return any(dfs(numbers, i + 1, option, result, operators) for option in options)

# Function to calculate the total sum for Part 1 (only using + and *)
def calculate_part_1(results, terms):
    total_sum_part_1 = 0  # Initialize the total sum for Part 1
    
    # Iterate through all results and terms
    for i in range(len(results)):
        result = results[i]  # Get the expected result for this equation
        # Start DFS from the second number (index 1), with the first number as the initial sum
        if dfs(terms[i], 1, terms[i][0], result, ['+', '*']):  # Start from the second number
            total_sum_part_1 += result  # Add the result to the total sum if a valid equation is found
    
    return total_sum_part_1

# Function to calculate the total sum for Part 2 (using +, *, and ||)
def calculate_part_2(results, terms):
    total_sum_part_2 = 0  # Initialize the total sum for Part 2
    
    # Iterate through all results and terms
    for i in range(len(results)):
        result = results[i]  # Get the expected result for this equation
        # Start DFS from the second number (index 1), with the first number as the initial sum
        if dfs(terms[i], 1, terms[i][0], result, ['+', '*', '||']):  # Start from the second number
            total_sum_part_2 += result  # Add the result to the total sum if a valid equation is found
    
    return total_sum_part_2

# Read input data
results, terms = read_input("input.txt")  # Read and parse the input file

# Calculate and print the result for Part 1
total_sum_part_1 = calculate_part_1(results, terms)
print("Part 1 Answer: {}".format(total_sum_part_1))

# Calculate and print the result for Part 2
total_sum_part_2 = calculate_part_2(results, terms)
print("Part 2 Answer: {}".format(total_sum_part_2))