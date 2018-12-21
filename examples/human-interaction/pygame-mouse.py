import pygame       # import pygame module
pygame.init()       # initialize all of pygame's submodules
screen = pygame.display.set_mode((400, 400))    # create a surface called 'screen' and give it a size of 400x400
running = True      # used to control while loop

while running:      # main loop of program. will repeat until the window is closed
    """Below this line is a for loop for handling the event queue.
    The event queue takes every event (user interaction) that happens in the pygame window and
    makes it available in order. the variable 'e' will be each event in order.
    Anything that involves handling events should generally happen in here"""
    
    for e in pygame.event.get():    # get each event in the event queue... 
        if e.type == pygame.QUIT:   # ...and if that event is QUIT...
            running = False         # ......set running to False so the main loop ends
        """The code below will print the coordinates of the mouse each time it moves and will
        draw a circle at the mouse's location each time a mouse button is pressed."""
        if e.type == pygame.MOUSEMOTION:        # if the event is mouse motion...
            print(pygame.mouse.get_pos())       # ...print the mouse's locaation
        if e.type == pygame.MOUSEBUTTONDOWN:    # if the event type is a button press...
            pygame.draw.circle(screen, (10, 70, 255), pygame.mouse.get_pos(), 20)  # draw a blue circle with radius 20 at the mouse's position

    """It's probably worth noting that we're still in the main loop here, but have left the for loop  
    for the event queue. This will run on repeat, but won't repeat for each event."""
    pygame.display.flip()               # update the display