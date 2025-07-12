import pygame
import random

class PowerUp:
    def __init__(self, x, y):
        self.type = random.choice(['speed', 'rapid'])
        self.image = pygame.image.load(f"assets/{self.type}.png").convert()
        self.image.set_colorkey((255, 255, 255))  # Remove white background
        self.x = x
        self.y = y
        self.speed = 3

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collides_with(self, player):
        return abs(self.x - player.x) < 32 and abs(self.y - player.y) < 32
