from enum import Enum

input = open("input.txt")
lines = input.readlines()
input.close()

# Data representing the input
grid:list[list[str]]=[]
# iteration variables
current_spot:tuple[int,int] = None
x = 0
y = 0
for line in lines:
    x = 1
    temp_list = []
    for char in line:
        if char != "\n":
            if char == '^':
                current_spot = (x,y)
            temp_list.append(char)
        x+=1
    grid.append(temp_list)
    y+=1

# Utility functions
def get_element(spot:tuple[int,int]):
    return grid[spot[0]][spot[1]]
def set_element(spot:tuple[int,int], new_value):
    grid[spot[0]][spot[1]] = new_value

def print_grid():
    for line in grid:
        print(("".join(line)))

def in_bounds(spot):
    return  0 < spot[0] < len(grid[0]) and 0 < spot[1] < len(grid)

# Direction to tuple Enum
class Direction(Enum):
    UP      = (-1,0)
    RIGHT   = (0,-1)
    DOWN    = (1,0)
    LEFT    = (0,1)

def next_direction(dir:Direction):
    match dir:
        case Direction.UP:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.LEFT
        case Direction.LEFT:
            return Direction.UP
        
direction=Direction.UP
left = False
while not left:
    set_element(current_spot, 'X')
    for _ in Direction:
        new_spot = current_spot[0] + direction.value[0], current_spot[1] + direction.value[1]
        if not in_bounds(new_spot):
            left=True
            break
        elif get_element(new_spot) == '#':
            direction = next_direction(direction)
    current_spot = new_spot
    print(new_spot)

total = 0
for line in grid:
    total += line.count('X')
print(total)

print_grid()