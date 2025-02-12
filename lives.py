import pygame
from constants import *


class Lives:
    def __init__(self):
        self.lives = 3
        self.lives_text = " <3"
        self.font = pygame.font.SysFont(SCORE_FONT, SCORE_SIZE)

    def draw(self, screen):
        text_surface = self.font.render(self.lives_text * self.lives, True, LIVES_COLOR)

        text_width = text_surface.get_width()
        screen.blit(
            text_surface,
            (SCREEN_WIDTH - text_width - LIVES_POSITION[0], LIVES_POSITION[1]),
        )

    def akshually(self):
        self.lives -= 1

    def get_lives(self):
        return self.lives
