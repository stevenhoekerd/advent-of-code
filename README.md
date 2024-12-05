# Advent of Code

## Day 1
### Silver
#### Algorithm:
NOTE: i misread the assignment, i thought the distance would have to be calculated using the index value in the inputlist, so i built it for that. woops.
still works fine, but the data structure is now a bit useless.

Quite a simple algorithm, it simply stores in 2 lists both of the entries in the inputline, and store along with it, its associated position.
Then we sort the whole thing, and simply compare elements from both lists at i for 1-1000.
Since we also store the position, we can then just take the abs of either positon minus the other, and sum the total.

#### Time complexity:
Time complexity: O(n log n)
- Iterating over each list to get input: O(n)
- Sorting the lists: O(n log n), since thats the complexity of the standard python sort.
- Iterating over lists to compare all entries: O(n), since we only need to loop over once and each element only gets compared once

### Gold
#### Algorithm:
i considered using a big list here and just incrementing by 1 at each index, but i didnt.
the setup is similair to the silver solution, and differs after the sort.
We iterate over the first list.
we Check whether the current entry in list 2 is larger, equal, or smaller.
- Equal: increment multiply value by 1, and go to the next value in list 2 and compare again.
- Larger: this means we're done with the current list1 value. add its value * multiply value to total, and go to the next list1 entry.
- Smaller: this means the current list2 value isnt needed anymore, and it means we've reached the max multi value for the current list1 value. get all entries from list 1 with this value, and do the same treatment as for larger.

#### Time complexity:
Probably O(n log n) again, due to the sort. i do do a whole lot of accessing entries in a list though, which might push me up a bit.
the algorithm itself is O(n log n ) though, and with optimizations it could easily reach that.

## Day 2 
### Silver
#### Algorithm:
A simple iteration over all lines, and checking the safety of each report.
We deem an entry unsafe if any of the following is true:
- an entry is equal to the previous
- the difference with the previous entry is over three
- the change goes in a different direction
we sum the amount of safe lines, and output it.

#### Time complexity:
O(n). Simple iteration, with a very linear opreation over it.

### Gold
#### Algorithm:
Same as for silver, expect besides testing every line, we also check each line with any element removed. if any of those are safe, we add 1 to the count of the total.

#### Time complexity
still O(n). a bit of a bigger calculation per n, but O(n) nonetheless.

## Day 3
### Silver
#### Algorithm:
Just a regex match, and an iteration.

#### Time complexity:
O(n). Simple iteration

### Gold
#### Algorithm:
Slightly bigger regex, and a bit more logic in the iteration over the result, but still not complicated

#### Time complexity
still O(n). a bit of a bigger calculation per n, but O(n) nonetheless.

## Day 4
### Silver
#### Algorithm:
create an X by Y grid out of the input, and pad all edges with an extra . to ensure we dont have to account for edges anywhere else.
If we find an x, we check all 8 directions for an M, and then AS in the same direction.


#### Time complexity:
O(n). quite an expensive one relatively speaking, but still O(n)

### Gold
#### Algorithm:
grid creation is the same, when iterating we now look for an A, and then we check its 4 relative positions for a cross, and check that we can create MAS twice.


#### Time complexity
still O(n). a bit less heavy than the silver solution even.


## Day 4
### Silver
#### Algorithm:
TODO




#### Time complexity:
TODO

### Gold
#### Algorithm:
TODO
#### Side Note:
Yeah i thougt "im gonna brute force this one:

```python
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


def brute_force(update):
    for permutation in permutations(update):  # Brute force baby
        val = check_update(permutation)
        if val > 0:
            return val
    return 0
```

Yeah no, immediately after running my laptop fans started spinning. didnt get a single line done.
O(n!) is  some crazy stuff.

#### Time complexity
TODO
