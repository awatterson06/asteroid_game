import asteroid
import asteroidfield
import player
import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event


def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock =pygame.time.Clock()
    dt = 0.0

    #creating groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #assign players in the Player class to containers 
    player.Player.containers = (updatable, drawable)
    #create player 1
    player1 = player.Player( x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT /2)  # noqa: F841

    #assign asteroids to the containers 
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)

    #assign the asteroid field to the updatable container as it's not an asteroid itself
    asteroidfield.AsteroidField.containers = (updatable,)

    #create an asteroid field
    field1 = asteroidfield.AsteroidField()

#create the game loop
    while True: 
        dt = game_clock.tick(60) /1000
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #update all game entities
        for entity in updatable:
            entity.update(dt)
            #detect if any asteroid has collided with the player 
            for rock in asteroids:
                if rock.collides_with(player1) == True:
                    log_event("player_hit")
                    print("Game Over!")
                    sys.exit()
        #redraw the game 
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        
        #print(f"{dt}")






if __name__ == "__main__":
    main()
