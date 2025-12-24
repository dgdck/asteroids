import pygame
from asteroid import Asteroid
from asteroidfield import Asteroidfield
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    # Add to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Asteroidfield.containers = (updatable)


    # Make Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = Asteroidfield()

    # Game loop
    while True:
        # Logging
        log_state()

        # Exit with window 'x'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update screen
        screen.fill("black")
        dt = Clock.tick(60) / 1000

        # Update objects
        updatable.update(dt)
        
        # Draw objects
        for object in drawable:
            object.draw(screen)
        
        # Display
        pygame.display.flip()


if __name__ == "__main__":
    main()
