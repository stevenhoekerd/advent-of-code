from datetime import datetime
from random import Random
# Read input
input = open("input.txt")
lines = input.readlines()
# define global lists
rule_list:list[(int,int)] = []
update_list:list[list[int]] = []
# Parse inputs
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

# -------------------------- END OF INIT --------------------------#

def generate_score(update):
    "Generates the penalty points for an update."
    past_list = []  # Keep track off all pages in this update
    fails = 0
    for page in update:
        rules = cummulative_rules[page] # Get all active rules for this page.
        rule_breaks = len(set(rules) & set(past_list))  # Get all pages that break a rule
        fails += rule_breaks    # sum of all fails.
        past_list.append(page)
    return fails


def get_middle(list):
    "Utility to get middle item of a list"
    return list[int(len(list) / 2)]


def check_one(faulty_update:list[int],best_score:int, a:int,b:int):
    "checks a neighbour. returns it if its better, otherwise returns the old"
    # Swap m
    faulty_update[a], faulty_update[b] = faulty_update[b], faulty_update[a]
    new_score = generate_score(faulty_update)
    if new_score < best_score: # Wow much improve!
        return (faulty_update,new_score), True
    else:   # if we didnt improve, undo the swap.
        faulty_update[a], faulty_update[b] = faulty_update[b], faulty_update[a]
        return (faulty_update,best_score), False

def check_them(faulty_update):
    rng = Random()
    for i in range(0,1000):
        r1 = rng.randint(0,len(faulty_update[0])-1)
        r2 = rng.randint(0,len(faulty_update[0])-1)
        faulty_update, improved = check_one(faulty_update[0],faulty_update[1],r1,r2)
        if faulty_update[1] == 0:
            return faulty_update
    return faulty_update


def optimize(faulty_update:list[int]):
    "Fix that thing"
    # Set the best score to the only one we know for now.
    
    best_score_tuple = (faulty_update, generate_score(faulty_update))
    while best_score_tuple[1] > 0:
        best_score_tuple = check_them(best_score_tuple)
    return best_score_tuple[0]

def main():
    # Now with all rules in place, loop over all updates
    total_value = 0
    progress = 0
    start_time = datetime.now()

    for update in update_list:
        progress += 1
        score = generate_score(update)
        if score == 0:  # If the score is 0, its already good so ignore.
            pass
        else:   # here the fun starts.
            total_value += get_middle(optimize(update))
    
    print(total_value)
    print(f"finished in {datetime.now() - start_time}")
main()