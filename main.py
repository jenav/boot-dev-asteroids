import pygame
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from shot import *
from score import *
from gameover import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Load background music
    pygame.mixer.music.load("sounds/background.mp3")
    pygame.mixer.music.play(-1, 0.0)

    # Load hit sound effect (roblox)
    hit_sound = pygame.mixer.Sound("sounds/hit.mp3")

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
    score = Score()
    state = STATE_RUNNING

    clock = pygame.time.Clock()
    dt = 0.0
    paused_timer = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if (
            pygame.key.get_pressed()[pygame.K_q]
            or pygame.key.get_pressed()[pygame.K_ESCAPE]
        ):
            return

        if paused_timer > 0:
            paused_timer -= dt
            if paused_timer < 0:
                paused_timer = 0

        if pygame.key.get_pressed()[pygame.K_p] and paused_timer == 0:
            paused_timer = 0.2
            if state == STATE_RUNNING:
                state = STATE_PAUSED
            else:
                state = STATE_RUNNING

        pygame.Surface.fill(screen, (0, 0, 0))

        if state == STATE_RUNNING:
            for u in updatable:
                u.update(dt)

            for a in asteroids:
                if a.check_collision(player):
                    hit_sound.play()
                    state = STATE_GAMEOVER
                    break
                for s in shots:
                    if a.check_collision(s):
                        s.kill()
                        a.split()
                        score.update()

        elif state == STATE_GAMEOVER:
            break

        for d in drawable:
            d.draw(screen)

        score.draw(screen, state)

        pygame.display.flip()
        dt = clock.tick(60) * 0.001

    pygame.time.delay(DELAY_AFTER_DEATH)
    pygame.mixer.music.stop()
    go = GameOver()
    go_sound = pygame.mixer.Sound("sounds/gameover.mp3")
    go_sound.play()
    go.show(screen, score.get_score(), clock)


if __name__ == "__main__":
    main()
