import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from shot import *
from score import *
from gameover import *
from helpers import *


def main():
    print("Starting Caquero Slayer!")
    print(f"Screen size: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Caquero Slayer")

    # Load background music
    pygame.mixer.music.load("sounds/background.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0)

    # Keep this dict small
    ctx = {
        "game_state": STATE_RUNNING,
        "music_state": MUSIC_PLAYING,
        "key_press_timer": 0.0,
        "pause_timer": 0.0,
    }

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

    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        # some important events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # to avoid key press repetition
        if ctx["key_press_timer"] > 0:
            ctx["key_press_timer"] -= dt

        hlp_handle_keys(pygame.key.get_pressed(), ctx)

        # timer de pausado temporal
        if ctx["pause_timer"] > 0:
            ctx["pause_timer"] -= dt
            if ctx["pause_timer"] <= 0:
                ctx["game_state"] = STATE_RUNNING

        pygame.Surface.fill(screen, (0, 0, 0))

        if ctx["game_state"] == STATE_EXITING:
            return

        if ctx["game_state"] == STATE_RUNNING:
            for u in updatable:
                u.update(dt)

            for a in asteroids:
                if a.check_collision(player):
                    player.get_hit()
                    if not player.is_alive():
                        ctx["game_state"] = STATE_GAMEOVER
                        break
                    else:
                        ctx["game_state"] = STATE_GOT_HIT
                        ctx["pause_timer"] = 1.0
                        a.kill()
                for s in shots:
                    if a.check_collision(s):
                        s.kill()
                        a.split()
                        score.update()

        if ctx["game_state"] == STATE_GAMEOVER:
            break

        for d in drawable:
            d.draw(screen)

        score.draw(screen, ctx["game_state"])
        player.draw_lives(screen)

        pygame.display.flip()
        dt = clock.tick(60) * 0.001

    # Game Over
    pygame.time.delay(DELAY_AFTER_DEATH)
    pygame.mixer.music.stop()
    go = GameOver()
    go_sound = pygame.mixer.Sound("sounds/gameover.mp3")
    go_sound.play()
    go.show(screen, score.get_score(), clock)


if __name__ == "__main__":
    main()
