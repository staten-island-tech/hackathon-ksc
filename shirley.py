import pygame
pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Dinosaur game")
background = pygame.image.load('downloads/pixlebg.jpg')

player_x = 100
player_y = 300
player_width = 50
player_height = 50
jumping = False

obstacle_x = 800
obstacle_y = 330
obstacle_width = 30
obstacle_height = 30


running = True 
while running:
    for event in pygame.event.get():
        screen.fill((235, 192, 230))
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True
            
     if jumping:
        player_y -= 5  
        if player_y <= 200:  
            jumping = False
    else:
        if player_y < 300:  
            player_y += 5
    
    obstacle_x -= 5
    if obstacle_x < -30: 
        obstacle_x = 800

    if dino_x < obstacle_x + obstacle_width and dino_x + dino_width > obstacle_x and dino_y + dino_height > obstacle_y:
        running = False
        
        
    ygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))
    
    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()