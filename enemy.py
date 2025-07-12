import pygame
import random

class Enemy:
    def __init__(self, speed=1):  # Accept speed as a parameter with a default value
        self.image = pygame.image.load("assets/enemy.png").convert_alpha()
        self.x = random.randint(0, 736)
        self.y = random.randint(30, 150)
        self.speed = speed  # Use the passed-in speed

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collides_with(self, bullet):
        enemy_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.image.get_width(), bullet.image.get_height())
        return bullet.active and bullet_rect.colliderect(enemy_rect)

    def reset(self):
        self.x = random.randint(0, 736)
        self.y = random.randint(30, 80)  # Spawn at the top again
