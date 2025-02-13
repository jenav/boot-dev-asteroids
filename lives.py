import pygame
from constants import *


class Lives:
    def __init__(self):
        self.lives = 3
        self.lives_text = f"x{self.lives}"
        self.lives_img = pygame.image.load(f"images/live.png").convert_alpha()
        self.font = pygame.font.SysFont(SCORE_FONT, SCORE_SIZE)

    def draw(self, screen):
        text_surface = self.font.render(self.lives_text, True, SCORE_COLOR)
        text_width = text_surface.get_width()

        screen.blit(
            self.lives_img,
            (
                SCREEN_WIDTH
                - self.lives_img.get_width()
                - text_width
                - 5
                - LIVES_POSITION[0],
                LIVES_POSITION[1],
            ),
        )

        screen.blit(
            text_surface,
            (SCREEN_WIDTH - text_width - LIVES_POSITION[0], LIVES_POSITION[1]),
        )

    def akshually(self):
        self.lives -= 1
        self.lives_text = f"x{self.lives}"

    def get_lives(self):
        return self.lives
