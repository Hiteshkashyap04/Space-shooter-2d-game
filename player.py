import pygame

class Player:
    def __init__(self, speed=5):
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.x = 370
        self.y = 480
        self.speed = speed

    def move_left(self):
        self.x -= self.speed
        self.x = max(self.x, 0)

    def move_right(self):
        self.x += self.speed
        self.x = min(self.x, 736)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
