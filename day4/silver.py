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
def get_next_letter(current_x, current_y):
    sucesses = 0
    
    for delta_x in range(-1,2):
        for delta_y in range(-1,2):
            if grid[current_x + delta_x][current_y + delta_y] == "M":
                if grid[current_x + 2 * delta_x][current_y + 2 * delta_y] == "A":
                    if grid[current_x + 3 * delta_x][current_y + 3 * delta_y] == "S":
                        sucesses += 1
    return sucesses

xmas_found = 0
for x in range(0, x_size):
    for y in range(0, y_size):
        char = grid[x][y]
        if char == "X":
            xmas_found += get_next_letter(x,y)
            
print(xmas_found)