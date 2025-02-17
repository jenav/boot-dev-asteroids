import pygame
from constants import *


def hlp_handle_keys(keys_pressed, ctx):
    if keys_pressed[pygame.K_q] or keys_pressed[pygame.K_ESCAPE]:
        ctx["game_state"] = STATE_EXITING

    if keys_pressed[pygame.K_p] and ctx["key_press_timer"] <= 0:
        ctx["key_press_timer"] = 0.2
        if ctx["game_state"] == STATE_RUNNING:
            ctx["game_state"] = STATE_PAUSED
            pygame.mixer.music.pause()
        else:
            ctx["game_state"] = STATE_RUNNING
            if ctx["music_state"] == MUSIC_PLAYING:
                pygame.mixer.music.unpause()

    if keys_pressed[pygame.K_m] and ctx["key_press_timer"] <= 0:
        ctx["key_press_timer"] = 0.2
        if ctx["music_state"] == MUSIC_PLAYING:
            pygame.mixer.music.pause()
            ctx["music_state"] = MUSIC_PAUSED
        else:
            pygame.mixer.music.unpause()
            ctx["music_state"] = MUSIC_PLAYING
