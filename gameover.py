import pygame
from constants import *


class GameOver:
    def __init__(self):
        self.gameover_font = pygame.font.SysFont(GAMEOVER_FONT, GAMEOVER_SIZE)
        self.score_font = pygame.font.SysFont(GAMEOVER_FONT, GAMEOVER_SIZE // 2)
        self.final_boss_img = pygame.image.load(
            f"images/final-boss.png"
        ).convert_alpha()

    def show(self, screen, score, game_clock):
        pygame.Surface.fill(screen, (20, 20, 20))

        gameover_surface = self.gameover_font.render("GAME OVER", True, GAMEOVER_COLOR)
        gameover_width = gameover_surface.get_width()
        gameover_height = gameover_surface.get_height()

        # render image first to set it in the background
        screen.blit(
            self.final_boss_img,
            (
                SCREEN_WIDTH / 2
                + gameover_width / 2
                - self.final_boss_img.get_width() / 2
                + 5,
                SCREEN_HEIGHT - self.final_boss_img.get_height() - 10,
            ),
        )

        screen.blit(
            gameover_surface,
            (
                SCREEN_WIDTH / 2 - gameover_width / 2,
                SCREEN_HEIGHT / 2 - gameover_height / 2,
            ),
        )

        score_surface = self.score_font.render(f"Score: {score}", True, GAMEOVER_COLOR)
        score_width = score_surface.get_width()
        score_height = score_surface.get_height()
        screen.blit(
            score_surface,
            (
                SCREEN_WIDTH / 2 - score_width / 2,
                SCREEN_HEIGHT / 2 + gameover_height - score_height / 2,
            ),
        )

        pygame.display.flip()

        # hold till the user quit
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            if (
                pygame.key.get_pressed()[pygame.K_q]
                or pygame.key.get_pressed()[pygame.K_ESCAPE]
            ):
                return
            game_clock.tick(60)
