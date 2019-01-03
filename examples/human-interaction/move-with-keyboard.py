import pygame
import sys
pygame.init()

x = 0
y = 0

screen = pygame.display.set_mode((400, 400))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            print("You pressed a key")
            print(f"Your key was {pygame.key.name(e.key)}")
            if pygame.key.name(e.key) == 'up':
                y -= 1
            if pygame.key.name(e.key) == 'down':
                y += 1
    
    print(f"Pacman is at {x}, {y}")