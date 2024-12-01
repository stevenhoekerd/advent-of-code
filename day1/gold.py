# Open file, and parse input
input = open("input.txt")
line = input.readline()

entry_list1 = []
entry_list2 = []

while line is not None:
    numbers = line.split()
    if len(numbers) == 0:
        break
    entry_list1.append(int(numbers[0]))
    entry_list2.append(int(numbers[1]))
    line = input.readline()

# Sort those lists based on their values
entry_list1.sort()
entry_list2.sort()

iterator_1 = 0
iterator_2 = 0
multiply_value = 0
total = 0

while iterator_1 < 1000:
    # If the value at i in list 1 equals that in list 2, we increase our multiplication value.
    if entry_list1[iterator_1] == entry_list2[iterator_2]:
        multiply_value += 1
        iterator_2 += 1 # In this scenario we havent reached the max. multi value, so we check another num from list 2
        continue
    elif entry_list1[iterator_1] > entry_list2[iterator_2]: # In this scenario we can ignore the current iterator_2 value, so we increase that.
        iterator_2 += 1
        continue
    elif entry_list1[iterator_1] < entry_list2[iterator_2]: # In this scenario we are done with the current iterator_1, so we add that value to the total.
        total += entry_list1[iterator_1] * multiply_value
        # all numbers with the same value need to also get this score
        if iterator_1 == 999:
            break
        while entry_list1[iterator_1] == entry_list1[iterator_1 + 1] and iterator_1 != 999:
            total += entry_list1[iterator_1 + 1] * multiply_value
            iterator_1 += 1
            if iterator_1 > 999:
                break
        multiply_value = 0
        iterator_1 += 1




print(total)