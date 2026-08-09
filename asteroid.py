import random

import constants
import logger
import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    """
    Represents an asteroid in the game.
    Inherits from CircleShape to handle physics and collision detection.
    """

    def __init__(self, x: float, y: float, radius: float) -> None:
        """
        Initializes an Asteroid at the given coordinates with a specified radius.
        """
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Renders the asteroid as a white circle on the provided screen surface.
        """
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        """
        Updates the asteroid's position based on its current velocity and delta time.
        """
        self.position += (self.velocity * dt)

    def split(self) -> None:
        """
        Handles the logic for splitting an asteroid upon impact.
        1. Removes the current asteroid from all groups.
        2. If the asteroid is at the minimum size, it just disappears.
        3. Otherwise, creates two new smaller asteroids rotating away from 
           the original trajectory.
        """
        self.kill()
        
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        logger.log_event("asteroid_split")
        
        # Calculate random angle for split trajectory
        random_angle = random.uniform(25, 50)

        # Rotate velocity vectors for the two new fragments
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        
        # Instantiate two smaller asteroids
        # We use self.__class__ to reference the Asteroid class dynamically
        for velocity in [v1, v2]:
            new_asteroid = self.__class__(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = velocity * 1.2
