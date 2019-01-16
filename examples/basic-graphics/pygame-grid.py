import pygame
import sys
import time
import random

pygame.init()

width = 600
height = 400

rows = 10
cols = 10

cell_height = height // rows
cell_width = width // cols


bg_color = (50, 20, 80)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("LIFE")

while True:
    for e in pygame.event.get():
        print(e)
        if e.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(bg_color)
    for row in range(rows):
        for cell in range(cols):
            if random.random() < .5:
                pygame.draw.rect(screen, (0, 0, 0), (cell * cell_width, row * cell_height, cell_width, cell_height))
            else:
                pygame.draw.rect(screen, (200, 200, 200), (cell * cell_width, row * cell_height, cell_width, cell_height))
    

    pygame.display.flip()
    time.sleep(1)
