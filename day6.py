import math
from typing import List

numbers = open('input_data/day6.txt', 'r').read().splitlines()

# Part one
operation_line = numbers[-1]
numbers = numbers[:-1]
numbers = [list(map(int, line.split())) for line in numbers]
operation_line = operation_line.split()

total_result = 0

for i in range(len(operation_line)):
    numbers_to_operate = []
    for j in range(len(numbers)):
        numbers_to_operate.append(numbers[j][i])

    operation = operation_line[i]
    if operation == '+':
        result = sum(numbers_to_operate)
    elif operation == '*':
        result = math.prod(numbers_to_operate)
    total_result += result

print(total_result)

# Part two
lines = []
with open('input_data/day6.txt', 'r') as file:
    for line in file:
        line = line.strip()
        lines.append(line)

total_result = 0

problems: List[List[str]] = []
operations = lines[-1].split()

digit_lines = lines[:-1]
line_length = max(len(line) for line in digit_lines)

problem = []
for i in range(line_length):
    value = 0

    all_spaces = True
    for line in digit_lines:
        if line[i].isdigit():
            value *= 10
            value += int(line[i])
            all_spaces = False

    if all_spaces:
        problems.append(problem)
        problem = []
    else:
        problem.append(value)
        value = 0

problems.append(problem)

for vs, op in zip(problems, operations):
    result = 0

    if op == "*":
        result = 1
        for v in vs:
            result *= int(v)
    else:
        for v in vs:
            result += int(v)

    total_result += result

print(total_result)