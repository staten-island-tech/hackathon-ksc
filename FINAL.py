import pygame
pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.Sdisplay.set_caption("KSC game")

background = pygame.image.load
background = pygame.transform.scale(background, (screen_width, screen_height))

jumping = False
falling = False

oval1_x = 100
oval1_y = 300
oval1_width = 120
oval1_height = 80
oval1_surface = pygame.Surface((oval1_width, oval1_height), pygame.SRCALPHA)
oval2_x = 1010
oval2_y = 275
oval2_width = 100
oval2_height = 60
oval2_surface = pygame.Surface((oval2_width, oval2_height), pygame.SRCALPHA)  # Use SRCALPHA for transparency
oval2_color = (125, 77, 31)
pygame.draw.ellipse(oval2_surface, oval2_color, (0, 0, oval2_width, oval2_height))


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

    screen.blit(background, (0, 0))  # Blit the background image
    screen.blit(oval1_surface, (oval1_x, oval1_y))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping and not falling:
        jumping = True
        jump_count = 20
    if jumping:
        oval1_y -= 5
        oval2_y -= 5
        jump_count -= 1
        if jump_count <= 0:
            jumping = False
            falling = True
    if falling:
        oval1_y += 5
        oval2_y += 5
        if oval1_y >= 300:
            oval1_y = 300
            oval2_y = 300
            falling = False

    obstacle_x -= 5
    if obstacle_x < -30: 
        obstacle_x = 800
        
        
    if (oval1_x < obstacle_x + obstacle_width and oval1_x + oval1_width > obstacle_x and oval1_y + oval1_height > obstacle_y):
        running = False

    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()