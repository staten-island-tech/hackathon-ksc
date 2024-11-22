import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Background Example')

# Load a background image (make sure the image exists in the same directory as the script)
background = pygame.image.load('pixel-background.jpg')  # Replace with your image file path
background = pygame.transform.scale(background, (screen_width, screen_height))  # Scale the background image to fit the window

# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user clicks the close button on the window
            running = False  # Stop the loop

    # Fill the screen with the background image
    screen.blit(background, (0, 0))  # Blit the background at position (0, 0)

    # Update the display
    pygame.display.flip()

# Quit Pygame and close the window
pygame.quit()
sys.exit()
