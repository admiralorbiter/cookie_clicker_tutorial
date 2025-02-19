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

# Upgrade button dimensions and position
button_x = 400
button_y = 300
button_width = 150
button_height = 50

cookies_per_second = 0  # Auto-generated cookies per second
upgrade_cost = 50  # Initial cost of the upgrade

# Set up the font
font = pygame.font.SysFont("Arial", 30)

# Initialize the score
score = 0

# Main game loop
running = True
while running:

    # Update the score based on cookies per second# Timer setup for auto-incrementing cookies
    clock = pygame.time.Clock()
    AUTO_INCREMENT_INTERVAL = 1000  # 1000 milliseconds = 1 second
    last_auto_increment = pygame.time.get_ticks()

    # Inside the game loop
    current_time = pygame.time.get_ticks()
    if current_time - last_auto_increment >= AUTO_INCREMENT_INTERVAL:
        score += cookies_per_second
        last_auto_increment = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the click is on the cookie
            if (cookie_x <= mouse_x <= cookie_x + cookie_size[0] and
                    cookie_y <= mouse_y <= cookie_y + cookie_size[1]):
                score += 1  # Increment the score

            # Check if the click is on the upgrade button
            elif (button_x <= mouse_x <= button_x + button_width and
                    button_y <= mouse_y <= button_y + button_height):
                if score >= 50:  # Upgrade costs 50 cookies
                    score -= 50  # Deduct the cost
                    cookies_per_second += 1  # Increase auto-click generati
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_ESCAPE:
                running = False

    # Fill the screen with a background color
    screen.fill((255, 255, 255))  # White background

    # Draw the cookie
    screen.blit(cookie_image, (cookie_x, cookie_y))

    # Render and display the score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))  # Black text
    screen.blit(score_text, (10, 10))  # Position: top-left corner

    # Draw the upgrade button
    pygame.draw.rect(screen, (0, 200, 0), (button_x, button_y, button_width, button_height))  # Green button
    button_text = font.render("Upgrade", True, (255, 255, 255))  # White text
    screen.blit(button_text, (button_x + 20, button_y + 10))  # Center text on the but

    # Display the upgrade cost
    cost_text = font.render(f"Cost: {upgrade_cost}", True, (0, 0, 0))  # Black text
    screen.blit(cost_text, (button_x, button_y - 30))  # Display above the button

    # Display cookies per second
    cps_text = font.render(f"Cookies/sec: {cookies_per_second}", True, (0, 0, 0))
    screen.blit(cps_text, (10, 50))  # Display below the score

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
