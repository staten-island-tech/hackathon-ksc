import pygame
pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Dinosaur game")
background = pygame.image.load('downloads/pixlebg.jpg')

player_width = 50
player_height = 50
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 1


running = True 
while running:
    for event in pygame.event.get():
        screen.fill((235, 192, 230))
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 0:
        player_x += player_speed
            
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))
    
    pygame.display.update()
pygame.quit()