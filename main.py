import pygame

from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
