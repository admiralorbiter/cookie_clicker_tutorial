# Import the Pygame library
import pygame

# Initialize Pygame
pygame.init()

# Set up the game window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the window caption
pygame.display.set_caption("Cookie Clicker")

# Main game loop
running = True
while running:
    # Check for events (e.g., window close)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color (e.g., white)
    screen.fill((255, 255, 255))  # RGB color for white

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()