import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("msg6723183026-36889.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("")
target_width = 50
target_height = 50

running = True
while running:
    pass

pygame.quit()