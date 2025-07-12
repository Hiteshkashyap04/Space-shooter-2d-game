import pygame

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.x = x
        self.y = y
        self.speed = 10
        self.is_fired = False
        self.active = False

    def fire(self, x, y):
        self.x = x + 16
        self.y = y
        self.is_fired = True
        self.active = True

    def move(self):
        if self.is_fired:
            self.y -= self.speed
            if self.y < 0:
                self.reset()

    def reset(self):
        self.is_fired = False
        self.active = False
        self.x = -100
        self.y = -100

    def draw(self, screen):
        if self.is_fired:
            screen.blit(self.image, (self.x, self.y))
