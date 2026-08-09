import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

    def collides_with(self, other) -> bool: 
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)

    """
    Collision detection logic:
    1. Calculate the Euclidean distance between the center points of the two circles:
       d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
       pygame's distance_to() method performs this calculation efficiently.
    2. Compare this distance to the sum of the two circles' radii.
       If the distance between centers is less than or equal to the sum of radii,
       the circles are overlapping or touching, indicating a collision.
    """