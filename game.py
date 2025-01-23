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

# Load the cookie image and set its size
cookie_image = pygame.image.load("cookie.png")
cookie_size = (100, 100)  # Width and height in pixels
cookie_image = pygame.transform.scale(cookie_image, cookie_size)

# Set the initial position of the cookie
cookie_x = 250  # Center horizontally (adjust based on window size)
cookie_y = 150  # Center vertically (adjust based on window size)

# Set up the font for displaying the score
font = pygame.font.SysFont("Arial", 30)  # Font name and size
# Initialize the score
score = 0

# Main game loop
running = True
while running:
    # Check for events (e.g., window close)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color (e.g., white)
    screen.fill((255, 255, 255))  # RGB color for white

    
    # Draw the cookie on the screen
    screen.blit(cookie_image, (cookie_x, cookie_y))

    # Render the score text
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))  # Black color
    screen.blit(score_text, (10, 10))  # Display at the top-left corner

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()