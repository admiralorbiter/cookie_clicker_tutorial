import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cookie Clicker")

# Load and resize the cookie image
cookie_image = pygame.image.load("cookie.png")
cookie_size = (100, 100)
cookie_image = pygame.transform.scale(cookie_image, cookie_size)
cookie_x = 250  # Horizontal position
cookie_y = 150  # Vertical position

# Set up the font
font = pygame.font.SysFont("Arial", 30)

# Initialize the score
score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position

            # Check if the click is on the cookie
            if (cookie_x <= mouse_x <= cookie_x + cookie_size[0] and
                    cookie_y <= mouse_y <= cookie_y + cookie_size[1]):
                score += 1  # Increment the score

    # Fill the screen with a background color
    screen.fill((255, 255, 255))  # White background

    # Draw the cookie
    screen.blit(cookie_image, (cookie_x, cookie_y))

    # Render and display the score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))  # Black text
    screen.blit(score_text, (10, 10))  # Position: top-left corner

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
