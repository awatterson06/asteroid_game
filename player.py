import pygame  # noqa: I001
from circleshape import CircleShape  # noqa: I001, RUF100
from constants import PLAYER_RADIUS, LINE_WIDTH ,SCREEN_WIDTH, SCREEN_HEIGHT  # noqa: F401

class Player(CircleShape):

    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        #super().draw(screen)
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)