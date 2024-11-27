import pygame
import sys


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Poo Poo')


background = pygame.image.load('pixel-background.jpg')  # Replace with your image file path
background = pygame.transform.scale(background, (screen_width, screen_height))  # Scale the background image to fit the window


oval1_width = 120
oval1_height = 80
oval1_surface = pygame.Surface((oval1_width, oval1_height), pygame.SRCALPHA)  # Use SRCALPHA for transparency


oval1_color = (125, 77, 31)
pygame.draw.ellipse(oval1_surface, oval1_color, (0, 0, oval1_width, oval1_height))  # Draw the first ellipse


oval2_width = 100
oval2_height = 60
oval2_surface = pygame.Surface((oval2_width, oval2_height), pygame.SRCALPHA)  # Use SRCALPHA for transparency


oval2_color = (125, 77, 31)
pygame.draw.ellipse(oval2_surface, oval2_color, (0, 0, oval2_width, oval2_height))  # Draw the second ellipse


x_pos1 = 100
y_pos1 = 400




x_pos2 = 110
y_pos2 = 375


# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user clicks the close button on the window
            running = False  # Stop the loop


    # Fill the screen with the background image
    screen.blit(background, (0, 0))  # Blit the background at position (0, 0)


    # Blit the first oval onto the screen at the updated position
    screen.blit(oval1_surface, (x_pos1, y_pos1))


    # Blit the second oval onto the screen at the updated position (on top of the first oval)
    screen.blit(oval2_surface, (x_pos2, y_pos2))
        # Update the display
    pygame.display.flip()


    # Limit the frame rate (optional, for smoother movement)
    pygame.time.Clock().tick(60)  # 60 frames per second


# Quit Pygame and close the window
pygame.quit()
sys.exit()

