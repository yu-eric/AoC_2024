
def patrol_path(grid):
    unique_positions = set()
    positions = [[-1, 0], [0, 1], [1, 0],  [0, -1]]
    direction = positions[0]
    position = [39, grid[39].index("^")] # our starting point

    while 0 <= position[0] < len(grid[0]) and 0 <= position[1] < len(grid):
        unique_positions.add(tuple(position))
        try:
            next_space = grid[position[0] + direction[0]][position[1] + direction[1]]
        except IndexError:
            return len(unique_positions)

        if next_space != "#":
            position[0] += direction[0]
            position[1] += direction[1]

        else:
            while next_space == "#":
                direction = (positions[positions.index(direction) + 1] if direction != [0, -1] else positions[0])
                next_space = grid[position[0] + direction[0]][position[1] + direction[1]]

            position[0] += direction[0]
            position[1] += direction[1]

    return len(unique_positions)


with open('6_input.txt') as f:
    grid = f.readlines()

print(patrol_path(grid))
