#!/usr/bin/env python3

from sympy import symbols, Eq, solve

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


def solve_claw_machine(a, b, prize):
    a1, a2 = a
    b1, b2 = b
    p1, p2 = prize

    a_presses, b_presses = symbols('a_presses b_presses')
    eq1 = Eq(a_presses * a1 + b_presses * b1, p1)
    eq2 = Eq(a_presses * a2 + b_presses * b2, p2)

    # Solve the first equation for a_presses
    solution_eq1 = solve(eq1, a_presses)

    # Substitute the solution of eq1 into eq2 and solve for b_presses
    substituted_eq2 = eq2.subs(a_presses, solution_eq1[0])
    solution_b = solve(substituted_eq2, b_presses)

    # Substitute the solution of b_presses back into eq1 to find a_presses
    solution_a = solve(eq1.subs(b_presses, solution_b[0]), a_presses)

    if solution_a and solution_b:
        # Calculate the total cost in tokens
        total_cost = solution_a[0] * 3 + solution_b[0]
        return total_cost
    else:
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
            total_cost += cost
            prizes_won += 1

    print(f"Prizes won: {prizes_won}")
    print(f"Total tokens spent: {total_cost}")
    return total_cost

# Convert the file into data that can be worked with.
machines = parse_input('input.txt')

# Solve Part one.
print(f"Part One Answer: {part_one(machines)}")