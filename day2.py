data = open('input_data/day2.txt', 'r').read()

lines = data.split(',')

# Part one
total_sum = 0

for line in lines:
    range_start, range_end = map(int, line.split('-'))

    for i in range(range_start, range_end + 1):
        if len(str(i)) % 2 != 0:
            pass
        
        first_half = str(i)[:len(str(i))//2]
        second_half = str(i)[len(str(i))//2:]

        if first_half == second_half:
            total_sum += i

print(total_sum)

# Part two
total_sum = 0

for line in lines:
    range_start, range_end = map(int, line.split('-'))

    for i in range(range_start, range_end + 1):
        if len(str(i)) % 2 != 0:
            pass
        
        number = str(i)
        number_length = len(number)

        for seq_len in range(1, number_length//2 + 1):
            if number_length % seq_len == 0:
                repeats = number_length // seq_len
                if repeats >= 2:
                    seq = number[:seq_len]
                    if seq * repeats == number:
                        total_sum += i
                        break

print(total_sum)