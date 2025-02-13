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
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0)

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
    pause_key_timer = 0.0
    pause_timer = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if (
            pygame.key.get_pressed()[pygame.K_q]
            or pygame.key.get_pressed()[pygame.K_ESCAPE]
        ):
            return

        # Timer para evitar repeticion de tecla de pausa
        if pause_key_timer > 0:
            pause_key_timer -= dt

        if pygame.key.get_pressed()[pygame.K_p] and pause_key_timer <= 0:
            pause_key_timer = 0.2
            if state == STATE_RUNNING:
                state = STATE_PAUSED
                pygame.mixer.music.pause()
            else:
                state = STATE_RUNNING
                pygame.mixer.music.unpause()

        # Timer de pausado temporal
        if pause_timer > 0:
            pause_timer -= dt
            if pause_timer <= 0:
                state = STATE_RUNNING

        pygame.Surface.fill(screen, (0, 0, 0))

        if state == STATE_RUNNING:
            for u in updatable:
                u.update(dt)

            for a in asteroids:
                if a.check_collision(player):
                    player.get_hit()
                    if not player.is_alive():
                        state = STATE_GAMEOVER
                        break
                    else:
                        state = STATE_GOT_HIT
                        pause_timer = 1.0
                        a.kill()
                for s in shots:
                    if a.check_collision(s):
                        s.kill()
                        a.split()
                        score.update()

        if state == STATE_GAMEOVER:
            break

        for d in drawable:
            d.draw(screen)

        score.draw(screen, state)
        player.draw_lives(screen)

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
