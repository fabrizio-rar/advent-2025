banks = open('input_data/day3.txt', 'r').read().strip().splitlines()

# Part one
total_joltage = 0

for bank in banks:
    largest_number = max(bank[:-1])
    largest_number_index = bank.index(largest_number)
    largest_number_2 = max(bank[largest_number_index + 1:])
    total_joltage = total_joltage + int(f"{largest_number}{largest_number_2}")

print(total_joltage)

# Part two
total_joltage = 0
battery_count = 12

for bank in banks:
    digits = []
    start_pos = 0
    
    for i in range(battery_count):
        remaining_digits = battery_count - i - 1
        end_pos = len(bank) - remaining_digits if remaining_digits > 0 else len(bank)
        search_range = bank[start_pos:end_pos]
        
        if not search_range:
            break
            
        largest_digit = max(search_range)
        digit_pos = bank.index(largest_digit, start_pos)
        digits.append(largest_digit)
        start_pos = digit_pos + 1
    
    if len(digits) == battery_count:
        total_joltage += int(''.join(digits))

print(total_joltage)