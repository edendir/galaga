import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load('/sprites/ship.png').convert_alpha()
        self.image = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
