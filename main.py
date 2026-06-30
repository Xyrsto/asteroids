import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)
    asteroid_field = AsteroidField()
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    pygame.init()
    while True:
        log_state()
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if (asteroid.collides_with(player)):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
