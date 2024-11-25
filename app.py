import pygame
pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Music game")

player_width = 50
player_height = 50
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

note_width = 30
note_height = 30
note_speed = 5
notes = []

running = True 
while running:
    for event in pygame.event.get():
        screen.fill((235, 192, 230))
        if event.type == pygame.QUIT:
            running = False

keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] and player_x > 0:
    player_x -= player_speed
if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
    player_x += player_speed


    
screen.fill((100, 0, 0))
pygame.display.update()
