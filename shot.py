"""The Shot class."""

import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    """Creates a Shot instance."""

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        """Draws the shot."""

        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        """Updates the shot's position."""
        
        self.position += self.velocity * dt