from itertools import permutations
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
    
def check_update(update):
    past_list = []  # Keep track off all pages in this update
    fail = False
    for page in update:
        rules = cummulative_rules[page] # Get all active rules for this page.
        if bool(set(rules) & set(past_list)):   # If any
            fail = True
            break
        past_list.append(page)
    
    return update[int(len(update) / 2)] if not fail else 0


def not_brute_force(update:list[int]):
    new_update:list[int] = []
    val = 0
    for page in update:
        if len(new_update) == 0:    # Base Case. no rules broken here
            new_update.append(page)
            continue
        # try inserting at any spot
        for i in range(0,len(new_update)+1):
            new_new_update = new_update.copy()
            new_new_update.insert(i,page)
            val = check_update(new_new_update)
            if val > 0:
                new_update = new_new_update
                break 
    return val

# Now with all rules in place, loop over all updates
total_value = 0
progress = 0
for update in update_list:
    progress += 1
    val = check_update(update)
    if val == 0:
        total_value += not_brute_force(update)
    


print(total_value)