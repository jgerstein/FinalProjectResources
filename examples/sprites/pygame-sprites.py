import pygame
import sys
import random

pygame.init()
w, h = 800, 500
screen = pygame.display.set_mode((w, h))

class Mouse(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("examples\\sprites\\mouse.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randrange(0, h)
    
    def update(self):
        self.rect.x += 1
        self.rect.y += random.randint(-5,5)

class Cat(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("examples\\sprites\\cat.png")
        self.rect = self.image.get_rect()
        self.rect.x = w//2
        self.rect.y = h//2
    
    def display(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
mouse_list = pygame.sprite.Group()
cat = Cat()


for n in range(30):
    mouse_list.add(Mouse())

while True:
    """Main loop of game"""

    for e in pygame.event.get():
        """Event queue handling"""
        if e.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((255, 255, 255))
    mouse_list.draw(screen)
    mouse_list.update()
    cat.display()

    pygame.display.flip()