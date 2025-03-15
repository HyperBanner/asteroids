"""Simple Asteroids implementation using pygame."""

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    """Main entrypoint into the program.
       Initializes pygame and a few other important variables,
       and sets up the the game loop."""

    # pygame
    pygame.init()

    # screensize
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # framerate related
    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    Shot.containers = (updatables, drawables, shots)

    # create important instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    # game loop
    while True:
        # if we trigger a quit event, close the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # background color
        screen.fill("black")

        # update the state of game objects
        updatables.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game Over!")
                return
            for shot in shots:
                if asteroid.collides(shot):
                    shot.kill()
                    asteroid.kill()

        # draw game objects
        for drawable in drawables:
            drawable.draw(screen)

        # redraw the screen and limit fps to 60
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
