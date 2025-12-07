fresh, availables = open("input_data/day5.txt", "r").read().strip().split('\n\n')

# Part one
fresh = [tuple(map(int, line.split('-'))) for line in fresh.splitlines()]
availables = [int(n) for n in availables.splitlines()]

total_fresh = sum(any(low <= a <= high for low, high in fresh) for a in availables)

print(total_fresh)

# Part two
fresh, _ = open("input_data/day5.txt", "r").read().strip().split('\n\n')
fresh = [tuple(map(int, line.split('-'))) for line in fresh.splitlines()]

fresh.sort()

merged_numbers = []
current_lower, current_upper = fresh[0]

for new_lower, new_upper in fresh[1:]:
    if new_lower <= current_upper + 1:
        current_upper = max(current_upper, new_upper)
    else:
        merged_numbers.append((current_lower, current_upper))
        current_lower, current_upper = new_lower, new_upper

merged_numbers.append((current_lower, current_upper))

fresh_numbers = sum(upper - lower + 1 for lower, upper in merged_numbers)
print(fresh_numbers)