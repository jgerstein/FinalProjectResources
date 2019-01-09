import pygame       # import pygame module
import os
import random
pygame.init()       # initialize all of pygame's submodules
screen = pygame.display.set_mode((400, 400))    # create a surface called 'screen' and give it a size of 400x400
running = True      # used to control while loop

x = 200
y = 200

img = pygame.image.load('examples\\basic-graphics\\img\\scarypacman.png')

while running:      # main loop of program. will repeat until the window is closed
    """Below this line is a for loop for handling the event queue.
    The event queue takes every event (user interaction) that happens in the pygame window and
    makes it available in order. the variable 'e' will be each event in order.
    Anything that involves handling events should generally happen in here"""
    
    for e in pygame.event.get():    # get each event in the event queue... 
        if e.type == pygame.QUIT:   # ...and if that event is QUIT...
            running = False         # ......set running to False so the main loop ends
    
    screen.fill((0,0,0))

    screen.blit(img, (x, y))
    x += random.randint(-5, 5)
    y += random.randint(-5, 5)
    if x < 0:
        x = 400
    elif x > 400:
        x = 0
    if y < 0:
        y = 400
    elif y > 400:
        y = 0
    
    pygame.display.flip()