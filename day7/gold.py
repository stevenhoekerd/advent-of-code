import itertools
input = open("input.txt")
lines = input.read().splitlines()

class Line:
    goal:int
    values = list[int]
    
    # Parse Logics
    def __init__(self, line:str):
        splits = line.split(":")
        self.goal = int(splits[0])
        self.values = [int(n) for n in splits[1].split()]

    def brute_force(self):
        op_list:list[str] = []
        for _ in range(1,len(self.values)): # get the starting operators
            op_list.append("+")
        
        if self.check_single(op_list):
            return self.goal
        
        iterator = itertools.product("+*|", repeat=(len(self.values) - 1))
        for string in iterator:
            if self.check_single(string):
                return True
        return False

    def check_single(self, operators:list[str]):
        intermediate = self.values[0]
        for i in range(1,len(self.values)):
            if operators[i-1] == "+":
                intermediate += self.values[i]
            elif operators[i-1] == "*":
                intermediate *= self.values[i]
            else:
                intermediate = int(f"{intermediate}{self.values[i]}")
        return self.goal == intermediate


line_list: list[Line] = []
for line in lines:
    line_list.append(Line(line))

total = 0
for line in line_list:
    if line.brute_force():
        total += line.goal  

print(total)