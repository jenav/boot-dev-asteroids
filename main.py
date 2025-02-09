import pygame
from constants import *
from circleshape import *
from player import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            return

        pygame.Surface.fill(screen, (0, 0, 0))
        for u in updatable:
            u.update(dt, keys)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) * 0.001


if __name__ == "__main__":
    main()
    print("Exiting...")
