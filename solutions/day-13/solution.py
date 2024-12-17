#!/usr/bin/env python3

from sympy import solve, Symbol

# This is the offset for Part Two.
OFFSET = 10^13

def parse_input(filename):
    # Open the file and read it to data.
    with open(filename, 'r') as input_file:
        data = input_file.read().strip().split('\n')

    # make an array for each machine, containing a dict for the respective values.
    machines = []
    # The input dictates a newline on the four, alongside the three lines we care about.
    for i in range(0, len(data), 4):
        # Extract the values we need.
        a = [int(x.split('+')[1]) for x in data[i].split(',')]
        b = [int(x.split('+')[1]) for x in data[i + 1].split(',')]
        prize = [int(x.split('=')[1]) for x in data[i + 2].split(',')]
        machines.append({
            'button_a': a,
            'button_b': b,
            'prize': prize
        })

    return machines


# The solution developed for part one didn't work here, so I looked into the SumPy library.
def solve_claw_machine_part_2(a, b, prize):
    a1, a2 = a
    b1, b2 = b
    p1, p2 = prize

    # Define as symbols for SumPy solve.
    a = Symbol("a", integer=True)
    b = Symbol("b", integer=True)
    
    # Shift the prize values for part 2
    OFFSET = 10**13
    p1 += OFFSET
    p2 += OFFSET

    # Use sympy's solve function to solve the system of equations.
    roots = solve(
        [a1 * a + b1 * b - p1, a2 * a + b2 * b - p2],
        [a, b]
    )
    
    if roots:
        # Extract the solution for a and b
        a_count, b_count = roots[a], roots[b]

        # If both a_count and b_count are non-negative integers
        if a_count >= 0 and b_count >= 0:
            total_cost = 3 * a_count + b_count
            return total_cost

    return None


def solve_claw_machine(a, b, prize):
    a1, a2 = a
    b1, b2 = b
    p1, p2 = prize

    for a_count in range(101):
        for b_count in range(101):
            # If both conditions are met, it returns:
            #  - The number of presses for each button (a_count and b_count).
            #  - The total cost, calculated as 3 * a_count + b_count
            #    (3 units for each press of button A, 1 unit for each press of button B).
            if a_count * a1 + b_count * b1 == p1 and a_count * a2 + b_count * b2 == p2:
                return a_count, b_count, 3 * a_count + b_count

    # No solution is found.
    return None


def part_one(machines):
    total_cost = 0
    prizes_won = 0

    # iterate through each machine.
    for machine in machines:
        # Solve the machine, giving the right values.
        cost = solve_claw_machine(machine['button_a'], machine['button_b'], machine['prize'])
        # The function returns None if no matches are found.
        if cost is not None:
            total_cost += cost[2]
            prizes_won += 1

    return total_cost

def part_two(machines):
    total_cost = 0
    prizes_won = 0

    # Iterate through each machine
    for machine in machines:
        cost = solve_claw_machine_part_2(machine['button_a'], machine['button_b'], machine['prize'])
        if cost is not None:
            total_cost += cost
            prizes_won += 1

    return total_cost

# Convert the file into data that can be worked with.
machines = parse_input('input.txt')

# Solve.
print(f"Part One Answer: {part_one(machines)}")
print(f"Part Two Answer: {part_two(machines)}")