import re
input = open("input.txt")
lines = input.readlines()

def use_regex(input):
    pattern = re.compile(r"mul\(([0-9]+),([0-9]+)\)|(don't\(\))|(do\(\))")
    
    return pattern.findall(input)

all_matches = []
for line in lines:
    matches = use_regex(line)
    all_matches += matches

enabled = 1
total = 0
for match in all_matches:
    if match[0] !='':
        total += (int(match[0]) * int(match[1])) * enabled
    if match[2] != '':
        enabled = 0
    if match[3] != '':
        enabled = 1
    
print(total)