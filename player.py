"""The Player class."""

import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *


class Player(CircleShape):
    """Creates the Player instance."""

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        """Math for getting the triangle shape."""

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Draws the triangle from triangle()."""

        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        """Rotate logic."""

        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """Move logic."""

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(*self.position)
        shot.velocity = pygame.math.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        """Updates player position based on the controls."""

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
        self.timer -= dt