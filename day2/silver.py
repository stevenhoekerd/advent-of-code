input = open("input.txt")
lines = input.readlines()

all_lists = []

for line in lines:
    numbers = line.split()
    number_list = []
    for number in numbers:
        number_list.append(int(number))
    all_lists.append(number_list)


def is_safe(single_line) -> bool:
    direction = 0
    last_entry = -1
    for entry in single_line:
        if last_entry == -1:
            last_entry = entry
            continue
        elif last_entry == entry:   # If 2 entries are the same, its unsafe
            return False
        
        # Increase/decrease check
        if direction == 0:
            direction = 1 if entry > last_entry else -1
        elif direction == -1:
            if entry > last_entry:
                return False
        elif direction == 1:
            if entry < last_entry:
                return False
        # max delta check
        if not 0 < abs(last_entry - entry) < 4:
            return False
        last_entry = entry
        
    return True

safes = 0
for list in all_lists:
    if is_safe(list):
        safes += 1

print(safes)