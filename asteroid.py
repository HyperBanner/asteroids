"""The Asteroid class."""

import random
import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    """Creates an Asteroid instance."""

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Draws the asteroid."""

        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """Updates the position of the asteroid."""

        self.position += self.velocity * dt

    def split(self):
        """Determines how splitting an asteroid should be done."""

        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vect1 = self.velocity.rotate(random_angle)
            vect2 = self.velocity.rotate(-random_angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            new1 = Asteroid(self.position.x, self.position.y, radius)
            new2 = Asteroid(self.position.x, self.position.y, radius)
            new1.velocity = vect1 * 1.2
            new2.velocity = vect2 * 1.2