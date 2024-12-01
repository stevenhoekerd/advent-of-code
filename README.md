# advent-of-code

## Day 1
### Silver
#### Algorithm
Quite a simple algorithm, it simply stores in 2 lists both of the entries in the inputline, and store along with it, its associated position.
Then we sort the whole thing, and simply compare elements from both lists at i for 1-1000.
Since we also store the position, we can then just take the abs of either positon minus the other, and sum the total.

#### Time complexity
Time complexity: O(n log n)
- Iterating over each list to get input: O(n)
- Sorting the lists: O(n log n), since thats the complexity of the standard python sort.
- Iterating over lists to compare all entries: O(n), since we only need to loop over once and each element only gets compared once

### Gold