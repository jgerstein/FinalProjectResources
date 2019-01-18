import random

class Cell:

    def __init__(self, x, y, is_blank, value=" "):
        self.x = x
        self.y = y
        self.is_blank = is_blank
        if self.is_blank:
            self.value = "*"
        else:
            self.value = value
    
    def show_cell(self):
        print(self.value, end=" ")


class Grid:

    def __init__(self, rows, cols):
        self.grid = []
                
        for y in range(rows):
            row = []
            for x in range(cols):
                row.append(Cell(x, y, True))
            self.grid.append(row)
    
    def show_grid(self):
        for row in self.grid:
            for cell in row:
                cell.show_cell()
            print("")

grid = Grid(10, 5)
grid.show_grid()