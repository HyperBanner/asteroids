"""Main class of the game."""

import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """CircleShape class. Collision gets calculated here."""

    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """Parent draw method, childs override this."""
        # sub-classes must override

    def update(self, dt):
        """Parent update method, childs override this."""
        # sub-classes must override

    def collides(self, circle):
        """Collision logic. This gets called in the game loop."""
        if self.position.distance_to(circle.position) <= self.radius + circle.radius:
            return True
        return False
