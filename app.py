import pygame

pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Game")

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((235, 192, 230))