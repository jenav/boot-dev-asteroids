import pygame
from constants import *


class Score:
    def __init__(self):
        self.score = 0
        self.score_text = f"Score: {self.score}"
        self.font = pygame.font.SysFont(SCORE_FONT, SCORE_SIZE)

    def draw(self, screen, state):
        if state == STATE_RUNNING:
            text_surface = self.font.render(self.score_text, True, SCORE_COLOR)
            screen.blit(text_surface, SCORE_POSITION)
        if state == STATE_PAUSED:
            text_surface = self.font.render("PAUSED", True, SCORE_COLOR)
            screen.blit(text_surface, SCORE_POSITION)

    def update(self):
        self.score += 20
        self.score_text = f"Score: {self.score}"

    def get_score(self):
        return self.score
