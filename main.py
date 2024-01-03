import pygame
from ship import Ship

DISPLAY = pygame.display.set_mode((640, 480))
FPS = 60
CLOCK = pygame.time.Clock()

PLAYER = Ship()

SPRITE_GROUP = pygame.sprite.Group()
SPRITE_GROUP.add(PLAYER)

running = True
while running:
    #Tick clock to maintain framerate
    CLOCK.tick(FPS)

    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #Update all the objects

    #Render display
    pygame.display.update()

