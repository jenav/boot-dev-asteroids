import pygame
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from shot import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if pygame.key.get_pressed()[pygame.K_q]:
            return

        pygame.Surface.fill(screen, (0, 0, 0))

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if a.check_collision(player):
                print("Game over!")
                return
            for s in shots:
                if a.check_collision(s):
                    s.kill()
                    a.split()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) * 0.001


if __name__ == "__main__":
    main()
    print("Exiting...")
