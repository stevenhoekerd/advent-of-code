input = open("input.txt")
lines = input.readlines()

# Creating a grid we can work with
grid = []

for line in lines:
    grid.append(list("." + line[:-1] + "."))

grid.insert(0, list("." * 142))
grid.append(list("." * 142))

x_size = len(grid[0])
y_size = len(grid)

# Function that, given an x and y with an X on it, checks all 8 diredctions for the MAS part
def get_cross(start_x, start_y):
    top_left = (grid[start_x-1][start_y-1],grid[start_x+1][start_y+1])
    top_right = (grid[start_x-1][start_y+1],grid[start_x+1][start_y-1])
    success = (
        (
            (top_left[0] == "M" and top_left[1] == "S")
            or
            (top_left[0] == "S" and top_left[1] == "M")
        )
        and
        (
            (top_right[0] == "M" and top_right[1] == "S")
            or
            (top_right[0] == "S" and top_right[1] == "M")
        )
    )    
    return success

xmas_found = 0
for x in range(0, x_size):
    for y in range(0, y_size):
        char = grid[x][y]
        if char == "A":
            xmas_found += 1 if get_cross(x,y) else 0
            
print(xmas_found)