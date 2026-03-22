import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    font = pygame.font.Font(None, 36)
    WHITE = (255, 255, 255)
    lives = 1

    score = 0
    def show_score(x, y):
        score_surface = font.render("Score: " +str(score), True, WHITE)
        screen.blit(score_surface, (x, y))

    def show_lives(x, y):
        lives_surface = font.render("Lives: " +str(lives), True, WHITE)
        screen.blit(lives_surface, (x, y))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field =AsteroidField()



    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        show_score(10, 10)
        show_lives(1150, 10)
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                if lives > 0:
                    player.kill()
                    lives -= 1
                    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
                else:
                    print("Game over!")
                    print("Final Score: ", score)
                    sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    score += 1
        pygame.display.flip()

        

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
            
if __name__ == "__main__":
    main()
