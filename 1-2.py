import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cookie Clicker")

# -------------------------------
# Add this: Load and resize cookie image
# -------------------------------
cookie_image = pygame.image.load("cookie.png")
cookie_size = (100, 100)  # Width and height of the cookie
cookie_image = pygame.transform.scale(cookie_image, cookie_size)
cookie_x = 250  # Horizontal position
cookie_y = 150  # Vertical position

# -------------------------------
# Add this: Set up the font
# -------------------------------
font = pygame.font.SysFont("Arial", 30)

# -------------------------------
# Add this: Initialize the score
# -------------------------------
score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color
    screen.fill((255, 255, 255))  # White background

    # ---------------------------------
    # Add this: Draw the resized cookie
    # ---------------------------------
    screen.blit(cookie_image, (cookie_x, cookie_y))

    # ---------------------------------
    # Add this: Render and display score
    # ---------------------------------
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))  # Black text
    screen.blit(score_text, (10, 10))  # Position: top-left corner

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
