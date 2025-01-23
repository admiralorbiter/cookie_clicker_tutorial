# Import the Pygame library
import pygame
import json  # Add this with the other imports at the top

# Initialize Pygame
pygame.init()

# Initialize the Pygame mixer for audio
pygame.mixer.init()

# Load the click sound
click_sound = pygame.mixer.Sound("click.mp3")

# Optionally, load background music
pygame.mixer.music.load("background.wav")

# Play the background music on a loop
pygame.mixer.music.play(loops=-1)

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

# Upgrade button dimensions and position
button_x = 400
button_y = 300
button_width = 150
button_height = 50

# Timer setup for auto-incrementing cookies
clock = pygame.time.Clock()
AUTO_INCREMENT_INTERVAL = 1000  # 1000 milliseconds = 1 second
last_auto_increment = pygame.time.get_ticks()


num_upgrades = 0    # Track the number of upgrades purchased
cookies_per_second = 0  # Auto-generated cookies per second
# Calculate the upgrade cost
upgrade_cost = int(50 * (1.2 ** num_upgrades))  # Base cost grows exponentially

fade_effects = []  # List to store fading circle
cookie_bounce = {"scale": 1.0, "direction": 1}

# Add these functions before the main game loop
def save_game(score, cookies_per_second, num_upgrades):
    save_data = {
        "score": score,
        "cookies_per_second": cookies_per_second,
        "num_upgrades": num_upgrades
    }
    with open("save_file.json", "w") as save_file:
        json.dump(save_data, save_file)

def load_game():
    try:
        with open("save_file.json", "r") as save_file:
            return json.load(save_file)
    except FileNotFoundError:
        return None

# Load saved game data at startup
saved_data = load_game()
if saved_data:
    score = saved_data["score"]
    cookies_per_second = saved_data["cookies_per_second"]
    num_upgrades = saved_data["num_upgrades"]

# Main game loop
running = True
while running:
    # Detect mouse click events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the click is on the cookie
            if (cookie_x <= mouse_x <= cookie_x + cookie_size[0] and
                    cookie_y <= mouse_y <= cookie_y + cookie_size[1]):
                score += 1  # Increment the score
                click_sound.play()  # Play the click sound
                cookie_bounce["direction"] = -1  # Start shrinking the cookie
                fade_effects.append({"x": mouse_x, "y": mouse_y, "radius": 10, "alpha": 255})  # Start a fade effect

            # Check if the click is on the upgrade button
            elif (button_x <= mouse_x <= button_x + button_width and
                    button_y <= mouse_y <= button_y + button_height):
                if score >= upgrade_cost:  # Check if the player can afford the upgrade
                    score -= upgrade_cost  # Deduct the cost
                    num_upgrades += 1  # Increment the number of upgrades
                    cookies_per_second += 1  # Increase auto-click speed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_s:  # Press 'S' to save
                save_game(score, cookies_per_second, num_upgrades)

    # Inside the game loop
    current_time = pygame.time.get_ticks()
    if current_time - last_auto_increment >= AUTO_INCREMENT_INTERVAL:
        score += cookies_per_second
        last_auto_increment = current_time

    # Fill the screen with a background color (e.g., white)
    screen.fill((255, 255, 255))  # RGB color for white
    for effect in fade_effects[:]:
        # Draw the fading circle
        surface = pygame.Surface((400, 400), pygame.SRCALPHA)  # Transparent surface
        pygame.draw.circle(surface, (255, 0, 0, effect["alpha"]), (effect["x"], effect["y"]), effect["radius"])
        screen.blit(surface, (0, 0))

        # Update effect properties
        effect["radius"] += 2
        effect["alpha"] -= 10
        if effect["alpha"] <= 0:
            fade_effects.remove(effect)  # Remove when completely faded

        if cookie_bounce["direction"] != 0:
            cookie_bounce["scale"] += 0.05 * cookie_bounce["direction"]
            if cookie_bounce["scale"] <= 0.9:
                cookie_bounce["direction"] = 1  # Start expanding
            elif cookie_bounce["scale"] >= 1.0:
                cookie_bounce["direction"] = 0  # Stop bouncing

    scaled_cookie = pygame.transform.scale(cookie_image, (int(cookie_size[0] * cookie_bounce["scale"]), int(cookie_size[1] * cookie_bounce["scale"])))
    screen.blit(scaled_cookie, (cookie_x, cookie_y))

    # Render the score text
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))  # Black color
    screen.blit(score_text, (10, 10))  # Display at the top-left corner
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

    # Display the number of upgrades purchased
    upgrades_text = font.render(f"Upgrades: {num_upgrades}", True, (0, 0, 0))  # Black text
    screen.blit(upgrades_text, (button_x, button_y + button_height + 10))  # Below the button
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()