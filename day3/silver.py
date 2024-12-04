import re
input = open("input.txt")
lines = input.readlines()

def use_regex(input):
    pattern = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
    
    return pattern.findall(input)

all_matches = []
for line in lines:
    matches = use_regex(line)
    all_matches += matches

total = 0
for match in all_matches:
    total += (int(match[0]) * int(match[1]))
print(total)  