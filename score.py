import pygame
from constants import *


class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(SCORE_FONT, SCORE_SIZE)

    def draw(self, screen):
        text_surface = self.font.render(f"Score: {self.score}", True, SCORE_COLOR)
        screen.blit(text_surface, SCORE_POSITION)

    def update(self):
        self.score += 20
