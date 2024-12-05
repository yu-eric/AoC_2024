def search(word, x, y, xn, yn, grid):
    if word[0] != grid[x][y]:
        return 0
    elif len(word) == 1 and word == grid[x][y]:
        return 1

    # Check if the new coordinates are within the bounds of the grid
    next_x = x + xn
    next_y = y + yn
    if not (0 <= next_x < len(grid)) or not (0 <= next_y < len(grid[0])):
        return 0

    return search(word[1:], next_x, next_y, xn, yn, grid)

def mas_search(x, y, grid):
    if not (0 <= x + 1 < len(grid)) or not (0 <= y + 1 < len(grid[0])) or not (0 <= x - 1 < len(grid)) or not (0 <= y - 1 < len(grid[0])):
        return 0

    elif grid[x][y] == "A" and (
        ((grid[x - 1][y + 1] == "M" and grid[x + 1][y - 1] == "S")  
        or (grid[x - 1][y + 1] == "S" and grid[x + 1][y - 1] == "M")) and
        ((grid[x - 1][y - 1] == "M" and grid[x + 1][y + 1] == "S")  
        or (grid[x - 1][y - 1] == "S" and grid[x + 1][y + 1] == "M"))
        ):
        return 1
    else:
        return 0
    

def cw_loop(word, grid):
    count = 0
    directions = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for xn, yn in directions:
                try:
                    count += search(word, x, y, xn, yn, grid)
                except IndexError as e:
                    print(f"IndexError at ({x}, {y}) with direction ({xn}, {yn}): {e}")
    return count

def mas_loop(grid):
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            count += mas_search(x, y, grid)
    return count

with open('4_input.txt') as f:
    xmas_grid = f.readlines()

print(cw_loop("XMAS", xmas_grid))
print(mas_loop(xmas_grid))
