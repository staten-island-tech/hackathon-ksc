import pygame
pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("KSC game") 

background = pygame.image.load('pixel-background.jpg')
background = pygame.transform.scale(background, (screen_width, screen_height))

pygame.mixer.music.load("audio.mp3") 
pygame.mixer.music.play(-1)
jump_sound = pygame.mixer.Sound("jump.wav")

jumping = False
falling = False

oval1_x = 100
oval1_y = 600  
oval1_width = 120
oval1_height = 80
oval1_color = (125, 77, 31)

oval2_width = 100
oval2_height = 60
oval2_color = (125, 77, 31)

obstacle_x = 800
obstacle_y = 625
obstacle_width = 30
obstacle_height = 30
obstacle_color = (255, 255, 255)

jump_count = 35

running = True 
while running:
    screen.fill((235, 192, 230))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))  

    pygame.draw.ellipse(screen, oval1_color, (oval1_x, oval1_y, oval1_width, oval1_height))
    
    oval2_y = oval1_y - oval2_height + 20  
    pygame.draw.ellipse(screen, oval2_color, (oval1_x + 10, oval2_y, oval2_width, oval2_height))

    pygame.draw.rect(screen, obstacle_color, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping and not falling:
        jumping = True
        jump_count = 35
    if jumping:
        oval1_y -= 5  
        jump_count -= 1
        if jump_count <= 0:
            jumping = False
            falling = True
            jump_sound.play()
    if falling:
        oval1_y += 5  
        if oval1_y >= 600:  
            oval1_y = 600
            falling = False
    obstacle_x -= 5
    if obstacle_x < -30:
        obstacle_x = 800
        
        
    if (oval1_x < obstacle_x + obstacle_width and oval1_x + oval1_width > obstacle_x and oval1_y + oval1_height > obstacle_y):
        running = False

    pygame.display.update()
    pygame.time.delay(30)
pygame.mixer.music.stop()
pygame.quit()