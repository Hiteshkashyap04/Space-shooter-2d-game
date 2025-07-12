import pygame
import random
from player import Player
from enemy import Enemy
from bullet import Bullet
from ui import show_score, game_over

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter")

bg = pygame.image.load("assets/space_bg.jpg")
bg = pygame.transform.scale(bg, (800, 600))

font = pygame.font.SysFont("arial", 32)
    

pygame.mixer.music.load("assets/background.ogg")
pygame.mixer.music.play(-1)

shoot_sound = pygame.mixer.Sound("assets/laser.ogg")
explosion_sound = pygame.mixer.Sound("assets/explosion.ogg")

player = Player(speed=7)
bullet = Bullet(-100, -100)

enemies = [Enemy(speed=1) for _ in range(3)]
score = 0
cooldown = 300  # milliseconds
last_shot = pygame.time.get_ticks()

game_over_line_y = 500
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    current_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and not bullet.is_fired and current_time - last_shot > cooldown:
        bullet.fire(player.x, player.y)
        shoot_sound.play()
        last_shot = current_time

    bullet.move()
    bullet.draw(screen)
    player.draw(screen)

    # Game over line
    pygame.draw.line(screen, (255, 255, 255), (0, game_over_line_y), (800, game_over_line_y), 2)

    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)

        if enemy.collides_with(bullet):
            explosion_sound.play()
            bullet.reset()
            enemies.remove(enemy)
            enemies.append(Enemy(speed=1))  # Spawn new enemy
            score += 1

        if enemy.y > game_over_line_y:
            game_over(screen, font)
            running = False

    show_score(screen, score, font)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
