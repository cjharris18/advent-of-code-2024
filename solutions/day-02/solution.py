#!/usr/bin/env python3

def create_list(report):
    # Convert the string to a list of integers
    return list(map(int, report.split()))


def is_increasing_or_decreasing(report):
    # Check if the report list is ascending.    
    # This uses list comprehension to see if report[i] is greater than or equal to report[i+1].
    # We use a for loop to iterate through the report.
    increasing = all(report[i] >= report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] <= report[i + 1] for i in range(len(report) - 1))

    # Check if they are increasing/decreasing or inconsistent.
    return True if increasing or decreasing else False

    
def check_differences(report):
    # Check through all the elements in our array.
    for i in range(len(report) - 1):
        # Taking the absolute values (remember we don't care about the direction, just the magnitude)..
        # Check if they increase by more than 3, if so return False.
        if not (1 <= abs(report[i] - report[i + 1]) <= 3):
            return False
    return True


def check_safe_report(report):
    # Function to check if the report is safe. Return a boolean True if safe, False if not.
    # Presume unsafe unless specified.
    outcome = False

    # Get the order of the report.
    order = is_increasing_or_decreasing(report)

    # Check the differences.
    difference = check_differences(report)

    # Check if it is increasing/decreasing and the differences are safe.
    if is_increasing_or_decreasing(report) and check_differences(report):
        outcome = True

    return outcome

# Lets start by setting the number of safe reports.
safe = 0

with open('input.txt', 'r') as input_file:
    # Iterate over each line in the file.
    for report in input_file:
        report_list = create_list(report.strip())  # .strip() to remove any trailing newline characters

        # Now we can check if an entry is safe:
        outcome = check_safe_report(report_list)

        # Incremement the value of safe. This works as the value of False is 0, and True is 1.
        safe += int(outcome)

# Print the solution answer.
print("Number of Safe Reports: {}".format(safe))
