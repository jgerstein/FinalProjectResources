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
    
    def make_word(self, word, direction, x, y):
        for n in range(len(word)):
            if direction == 'horizontal':
                self.grid[y][x+n].value = word[n]
            elif direction == 'vertical':
                self.grid[y+n][x].value = word[n]

    def show_grid(self):
        for row in self.grid:
            for cell in row:
                cell.show_cell()
            print("")
        print("-"*30)

grid = Grid(3, 5)
grid.show_grid()
grid.make_word('cat', 'horizontal', 0, 0)
grid.make_word('cow', 'vertical', 0, 0)
grid.show_grid()