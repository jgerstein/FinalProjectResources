# This is not fully documented because it was an example I worked through with a student.
# If you want to see the comments, please let me know.

import random

rows = 3
cols = 5

class Cell:

    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive
    
    def __str__(self):
        return f"{self.x}, {self.y}: {self.alive}"
    
    __repr__ = __str__

cells = []

for y in range(rows):
    row = []
    for x in range(cols):
        row.append(Cell(x, y, random.choice([True, False])))
    cells.append(row)

for row in cells:
    # print(row)
    for cell in row:
        if cell.alive:
            print('*', end=' | ')
        else:
            print(' ', end=' | ')
    print('')