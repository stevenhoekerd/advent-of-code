input = open("input.txt")
lines = input.readlines()

rule_list:list[(int,int)] = []
update_list:list[list[int]] = []

format_changed = False # After the empty line, the format changes from rules to entries
for line in lines:
    if line == "\n":
        format_changed = True
    elif format_changed:
        raw_list = line.split(",")
        update_list.append([int(x) for x in raw_list])  # parse n append
    else:
        nums = line.split("|")
        nums = [int(x) for x in nums]
        rule_list.append((nums[0],nums[1]))

# Dict with key i, returning list of n numbers that have to be before it
cummulative_rules:dict[int,list[int]] = {1:[]}
# Initialize ditct, filling all entries with an empty list
for i in range(2,100):
    cummulative_rules[i] = []

x = cummulative_rules[1]
for rule in rule_list:
    cummulative_rules[rule[0]].append(rule[1])
    
# Now with all rules in place, loop over all updates
total_value = 0
for update in update_list:
    past_list = []  # Keep track off all pages in this update
    fail = False
    for page in update:
        rules = cummulative_rules[page] # Get all active rules for this page.
        if bool(set(rules) & set(past_list)):   # If any
            fail = True
            break
        past_list.append(page)
    if not fail:
        total_value += update[int(len(update) / 2)]

print(total_value)