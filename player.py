import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH


class Player(CircleShape):

    WHITE = (255, 255, 255)

    def __init__(self, x, y):
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, self.WHITE, self.triangle(), 2)
        return super().draw(screen)
