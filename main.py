import pygame

# Define some constants

SCREEN_WIDTH = 640

SCREEN_HEIGHT = 480

# Define some colors

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

BLUE = (0, 0, 255)

# Define some sprites

PLAYER_SPRITE = pygame.image.load("player.png")

ALIEN_SPRITE_1 = pygame.image.load("alien_1.png")

ALIEN_SPRITE_2 = pygame.image.load("alien_2.png")

ALIEN_SPRITE_3 = pygame.image.load("alien_3.png")

POWERUP_SPRITE = pygame.image.load("powerup.png")

# Define some variables

player_x = SCREEN_WIDTH / 2

player_y = SCREEN_HEIGHT - PLAYER_SPRITE.get_height()

alien_x = 0

alien_y = 0

alien_speed = 1

alien_direction = 1

powerup_x = 0

powerup_y = 0

powerup_type = 0
score = 0

# Initialize Pygame

pygame.init()

# Create the screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window

pygame.display.set_caption("Space Invaders: The Last Stand")

# Create the background

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

background.fill(BLACK)

# Create the player sprite

player = pygame.sprite.Sprite()

player.image = PLAYER_SPRITE

player.rect = player.image.get_rect()

player.rect.centerx = player_x

player.rect.centery = player_y

# Create the alien sprites

aliens = []

for i in range(10):

    alien = pygame.sprite.Sprite()

    alien.image = ALIEN_SPRITE_1

    alien.rect = alien.image.get_rect()

    alien.rect.x = alien_x

    alien.rect.y = alien_y

    aliens.append(alien)

# Create the powerup sprite

powerup = pygame.sprite.Sprite()

powerup.image = POWERUP_SPRITE

powerup.rect = powerup.image.get_rect()

powerup.rect.x = powerup_x

powerup.rect.y = powerup_y
# Create the clock

clock = pygame.time.Clock()

# Start the main loop

while True:

    # Check for events

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            break

        # Check for key presses

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                player_x -= 5

            elif event.key == pygame.K_RIGHT:

                player_x += 5

            elif event.key == pygame.K_SPACE:

                player.shoot()

    # Update the player

    player.rect.centerx = player_x

    # Update the aliens

    for alien in aliens:

        alien.rect.x += alien_speed * alien_direction

        # Check if the aliens have reached the bottom of the screen

        if alien.rect.bottom >= SCREEN_HEIGHT:

            # The player has lost

            break

        # Check for collisions between the player and the aliens

        if player.rect.colliderect(alien.rect):

            # The player has lost

            break
            # Update the powerup

    powerup.rect.x += 1

    # Check for collisions between the player and the powerup

    if player.rect.colliderect(powerup.
                     # If the player has collected a powerup, update the player's stats

    if powerup_type == 1:

        player.speed += 1

    elif powerup_type == 2:

        player.health += 1

    elif powerup_type == 3:

        player.bullet_damage += 1

    # Remove the powerup from the game

    powerup.kill()

    # Draw the background

    screen.blit(background, (0, 0))

    # Draw the player

    screen.blit(player.image, player.rect)

    # Draw the aliens

    for alien in aliens:

        screen.blit(alien.image, alien.rect)

    # Draw the powerup

    screen.blit(powerup.image, powerup.rect)

    # Draw the score

    score_text = pygame.font.SysFont("comicsansms", 20).render("Score: " + str(score), True, WHITE)

    screen.blit(score_text, (10, 10))

    # Update the display

    pygame.display.update()

    # Check if the player has lost

    for alien in aliens:

        if alien.rect.colliderect(player.rect):

            # The player has lost

            break

    if alien:

        # The player has lost

        game_over()

    # Limit the framerate to 60 frames per second

    clock.tick(60)      
                 # If the player has lost, display the game over screen

    if alien:

        game_over()

    # Check if the player has won

    if len(aliens) == 0:

        # The player has won

        win()

    # Continue the main loop

    continue

def game_over():

    # Display the game over screen

    screen.fill(BLACK)

    game_over_text = pygame.font.SysFont("comicsansms", 100).render("Game Over", True, WHITE)

    screen.blit(game_over_text, (SCREEN_WIDTH / 2 - game_over_text.get_width() / 2, SCREEN_HEIGHT / 2 - game_over_text.get_height() / 2))

    pygame.display.update()

    # Wait for the player to press a key

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            elif event.type == pygame.KEYDOWN:

                return

def win():

    # Display the win screen

    screen.fill(BLACK)

    win_text = pygame.font.SysFont("comicsansms", 100).render("You Win!", True, WHITE)

    screen.blit(win_text, (SCREEN_WIDTH / 2 - win_text.get_width() / 2, SCREEN_HEIGHT / 2 - win_text.get_height() / 2))

    pygame.display.update()

    # Wait for the player to press a key

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            elif event.type == pygame.KEYDOWN:

                return       
                        # If the player has pressed a key, start a new game

    if event.key == pygame.K_SPACE:

        new_game()

# This is the main function that runs the game

def main():

    # Initialize Pygame

    pygame.init()

    # Create the screen

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the title of the window

    pygame.display.set_caption("Space Invaders: The Last Stand")

    # Create the background

    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    background.fill(BLACK)

    # Create the player sprite

    player = pygame.sprite.Sprite()

    player.image = PLAYER_SPRITE

    player.rect = player.image.get_rect()

    player.rect.centerx = SCREEN_WIDTH / 2

    player.rect.centery = SCREEN_HEIGHT - PLAYER_SPRITE.get_height()

    # Create the alien sprites

    aliens = []

    for i in range(10):

        alien = pygame.sprite.Sprite()

        alien.image = ALIEN_SPRITE_1

        alien.rect = alien.image.get_rect()

        alien.rect.x = alien_x

        alien.rect.y = alien_y

        aliens.append(alien)

    # Create the powerup sprite

    powerup = pygame.sprite.Sprite()

    powerup.image = POWERUP_SPRITE

    powerup.rect = powerup.image.get_rect()

    powerup.rect.x = powerup_x

    powerup.rect.y = powerup_y

    # Create the clock

    clock = pygame.time.Clock()    
                               # Start the main loop

    while True:

        # Check for events

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                break

            # Check for key presses

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:

                    player_x -= 5

                elif event.key == pygame.K_RIGHT:

                    player_x += 5

                elif event.key == pygame.K_SPACE:

                    player.shoot()

        # Update the player

        player.rect.centerx = player_x

        # Update the aliens

        for alien in aliens:

            alien.rect.x += alien_speed * alien_direction

            # Check if the aliens have reached the bottom of the screen

            if alien.rect.bottom >= SCREEN_HEIGHT:

                # The player has lost

                break

            # Check for collisions between the player and the aliens

            if player.rect.colliderect(alien.rect):

                # The player has lost

                break

        # Update the powerup

        powerup.rect.x += 1

        # Check for collisions between the player and the powerup

        if player.rect.colliderect(powerup.rect):

            # If the player has collected a powerup, update the player's stats

            if powerup_type == 1:

                player.speed += 1

            elif powerup_type == 2:

                player.health += 1

            elif powerup_type == 3:

                player.bullet_damage += 1

            # Remove the powerup from the game

            powerup.kill()
                     # Draw the background

        screen.blit(background, (0, 0))

        # Draw the player

        screen.blit(player.image, player.rect)

        # Draw the aliens

        for alien in aliens:

            screen.blit(alien.image, alien.rect)

        # Draw the powerup

        screen.blit(powerup.image, powerup.rect)
    # Draw the score

    score_text = pygame.font.SysFont("comicsansms", 20).render("Score: " + str(score), True, WHITE)

    screen.blit(score_text, (10, 10))

    # Update the display

    pygame.display.update()

    # Check if the player has lost

    for alien in aliens:

        if alien.rect.colliderect(player.rect):

            # The player has lost

            break

    if alien:

        # The player has lost

        game_over()

    # Check if the player has won

    if len(aliens) == 0:

        # The player has won

        win()

    # Limit the framerate to 60 frames per second

    clock.tick(60)

if __name__ == "__main__":

    main()
          
                               
