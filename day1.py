with open('input_data/day1.txt', 'r') as file:
    data = file.readlines()

# Part one
zero_amount = 0
current_position = 50

for line in data:
    direction = line[0]
    amount = int(line[1:])

    if direction == "L":
        current_position = (current_position - amount) % 100
    else:
        current_position = (current_position + amount) % 100
    
    if current_position == 0:
        zero_amount += 1

print(zero_amount)

# Part two
zero_amount = 0
current_position = 50

for line in data:
    direction = line[0]
    amount = int(line[1:])

    for _ in range(amount):
        if direction == "L":
            current_position = (current_position - 1) % 100
        else:
            current_position = (current_position + 1) % 100

        if current_position == 0:
            zero_amount += 1

print(zero_amount)