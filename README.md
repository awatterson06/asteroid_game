# Asteroids Game Documentation

This document provides a breakdown of the Pygame modules, classes, and functions used in the project, intended for those learning the library.

## Pygame Core Concepts

### `pygame.sprite.Sprite`

A base class for visible game objects. By inheriting from this class, our objects gain the ability to be managed by `pygame.sprite.Group` containers, which makes updating and drawing multiple objects efficient.

* **`self.add(*groups)`**: Adds the sprite to specific groups.
* **`self.kill()`**: Removes the sprite from all groups it belongs to (great for deleting off-screen bullets or destroyed asteroids).

### `pygame.sprite.Group`

A container class that holds `Sprite` objects.

* **`group.update(dt)`**: Automatically calls the `update()` method for every sprite contained in the group.
* **`group.draw(surface)`**: Automatically calls the `draw()` method (if defined as `image` and `rect`) for every sprite in the group.

---

## Classes and Methods

### `pygame.Vector2`

Used to represent 2D positions and velocities. It provides built-in math operators for vector addition, subtraction, and scaling.

* **`distance_to(other_vector)`**: Calculates the straight-line (Euclidean) distance between two points. Essential for our collision detection.
* **`x` and `y` attributes**: Directly access the coordinates.

### `pygame.Surface`

Represents an image or the main game window.

* **`screen.fill("color")`**: Clears the entire screen by filling it with a solid color.
* **`pygame.draw.circle(...)`**: Draws a circle on the surface. We use this to render our `CircleShape` objects (Player, Asteroids, Shots).

---

## Main Game Loop Functions

### Initialization

* **`pygame.init()`**: Initializes all imported pygame modules. Must be called before using other pygame functions.
* **`pygame.display.set_mode((width, height))`**: Creates the main window for the game.
* **`pygame.time.Clock()`**: Creates an object to track time, which is crucial for managing the game's frame rate.

### The Game Loop

* **`clock.tick(60)`**: This function does two things:
    1. It forces the loop to run at 60 frames per second (FPS).
    2. It returns the number of milliseconds that passed since the last call to `tick()`. We divide this by 1000 to get `dt` (delta time) in seconds.
* **`pygame.event.get()`**: Fetches all pending events (like keyboard presses or the user clicking "X" to close the window) from the event queue.
* **`pygame.display.flip()`**: Refreshes the display to show the drawings we've performed on the `screen` surface during this frame.

---

## Math & Physics

* **`dt` (Delta Time)**: The time passed since the last frame. By multiplying movement (velocity) by `dt`, our game objects move at the same speed regardless of how fast the computer is running the game.
* **Collision Detection**: We determine if two objects collide by checking if the distance between their centers is less than the sum of their radii:
    `distance <= (radius1 + radius2)`
