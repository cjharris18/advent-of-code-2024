#!/usr/bin/env python3

def create_list(report):
    # Convert the string to a list of integers
    return list(map(int, report.split()))

def is_increasing_or_decreasing(report):
    # Check if the report list is ascending or descending.
    increasing = all(report[i] <= report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] >= report[i + 1] for i in range(len(report) - 1))

    # Return True if the list is either increasing or decreasing.
    return increasing or decreasing

def check_differences(report):
    # Check if the differences between consecutive elements are within the range 1 to 3.
    return all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

def check_safe(report):
    # Check if the report is safe by verifying order and differences.
    return is_increasing_or_decreasing(report) and check_differences(report)

def part_two(report):
    # Check if removing one element makes the report safe.
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if check_safe(new_report):
            return True
    return False

# Initialize counters for safe reports.
safe, safe_p2 = 0, 0

with open('input.txt', 'r') as input_file:
    # Iterate over each line in the file.
    for report in input_file:
        report_list = create_list(report.strip())  # .strip() to remove any trailing newline characters

        # Check if the report is safe.
        if check_safe(report_list):
            safe += 1
        else:
            # Check if the report can be made safe by removing one element.
            if part_two(report_list):
                safe_p2 += 1

# Add the original safe reports to the ones found in part two.
safe_p2 += safe

# Print the solution answers.
print("Part One Answer: {}".format(safe))
print("Part Two Answer: {}".format(safe_p2))
