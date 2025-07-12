import pygame

def show_score(screen, score, font):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def game_over(screen, font):
    over_text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (300, 250))
