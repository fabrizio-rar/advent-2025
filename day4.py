data = open('input_data/day4.txt', 'r').read().strip().splitlines()

# Part one
accessible = 0
directions = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]

for index, line in enumerate(data):
    for char_index, char in enumerate(line):
        if char != '@':
            continue
        
        at_amount = 0
        for dy, dx in directions:
            new_row = index + dy
            new_col = char_index + dx
            
            if 0 <= new_row < len(data) and 0 <= new_col < len(line):
                if data[new_row][new_col] == '@':
                    at_amount += 1
        
        if at_amount < 4:
            accessible += 1

print(accessible)

# Part two
removable = 0

while True:
    to_remove = []
    for index, line in enumerate(data):
        for char_index, char in enumerate(line):
            if char != '@':
                continue
            
            at_amount = 0
            for dy, dx in directions:
                new_row = index + dy
                new_col = char_index + dx
                
                if 0 <= new_row < len(data) and 0 <= new_col < len(line):
                    if data[new_row][new_col] == '@':
                        at_amount += 1
            
            if at_amount < 4:
                to_remove.append((index, char_index))

    if len(to_remove) == 0:
        break

    for row, col in to_remove:
        data[row] = data[row][:col] + '.' + data[row][col+1:]
        removable += 1

print(removable)