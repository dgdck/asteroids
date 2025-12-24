import pygame
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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    # Add to groups
    Player.containers = (updatable, drawable)

    # Make Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = Clock.tick(60) / 1000
        # Update
        updatable.update(dt)
        
        # Draw objects
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()


if __name__ == "__main__":
    main()
