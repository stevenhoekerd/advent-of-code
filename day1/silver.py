# Open file, and parse input
input = open("input.txt")
line = input.readline()

entry_list1 = []
entry_list2 = []

i = 0
while line is not None:
    numbers = line.split()
    if len(numbers) == 0:
        break
    entry_list1.append(int(numbers[0]))
    entry_list2.append(int(numbers[1]))
    line = input.readline()
    i = i+1

# Sort those lists based on their values
entry_list1.sort()
entry_list2.sort()

# now we just iterate over them, we'll always have the lowest one next, so we can just directly compare.
total = 0
for i in range(0,1000):
    distance = abs(entry_list1[i] - entry_list2[i])
    total = total + distance

print(total)