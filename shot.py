import constants
import pygame
from circleshape import CircleShape


class Shot(CircleShape):
    """
    A projectile fired by the player.
    Inherits from CircleShape to utilize collision detection and 
    coordinate tracking properties.
    """

    def __init__(self, x: float, y: float):
        """
        Initializes a new Shot instance at a specific position.
        Uses SHOT_RADIUS from constants.py for the physical size.
        """
        super().__init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Overrides the CircleShape draw method.
        Renders the shot as a red circle on the provided screen surface.
        """
        pygame.draw.circle(screen, color="red", center=self.position, radius=self.radius, width=constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        """
        Overrides the CircleShape update method.
        Updates the shot's position by adding the current velocity 
        multiplied by the delta time (dt) for frame-rate independence.
        """
        self.position += self.velocity * dt
