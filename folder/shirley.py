import pygame
pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Jumping game")

player_x = 100
player_y = 300
player_width = 50
player_height = 50
jumping = False
falling = False

obstacle_x = 800
obstacle_y = 330
obstacle_width = 30
obstacle_height = 30
jump_count = 20

running = True 
while running:
    screen.fill((235, 192, 230))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping and not falling:
        jumping = True
        jump_count = 20
    if jumping:
        player_y -= 5  
        jump_count -= 1  
        if jump_count <= 0: 
            jumping = False
            falling = True
    if falling:
        player_y += 5
        if player_y >= 300:  
            player_y = 300
            falling = False

    obstacle_x -= 5
    if obstacle_x < -30: 
        obstacle_x = 800

    if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x and player_y + player_height > obstacle_y:
        running = False
        
        
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()