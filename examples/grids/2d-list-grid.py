grid = []

rows = 5
columns = 4

for y in range(0, rows):
    row = []
    for x in range(0, columns):
        # print(f"{x}, {y}", end=' | ')
        row.append(f"{x}, {y}")
    grid.append(row)

for row in grid:
    for cell in row:
        print(cell, end = ' | ')
    print('')

print(grid[0][1])
print("right:", grid[0][0])
print("left:", grid[0][2])