from copy import deepcopy
import copy
import pygame
import screens.gameevents
import fileutil
import guihelpers
import settings
from defs import *

# luodaan ruutu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Othello GUI")

ACTIVE_SCREEN = PLAY
game = screens.gameevents.GameEvents()
loader = fileutil.Loader()
options = settings.Settings()
# ns. Pelilooppi.
RUNNING = True
while RUNNING:
    # Tarkistetaan vain yrittaako kayttaja sulkea ohjelman.
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if guihelpers.cursor_on_text_box(ENGINE_MOVE_X, ENGINE_MOVE_Y, "Go Back", BUTTON_FONT):
                if ACTIVE_SCREEN == SETTINGS:
                    ACTIVE_SCREEN = PLAY
            if guihelpers.cursor_on_text_box(OPTIONS_X, OPTIONS_Y, OPTIONS_T, BUTTON_FONT):
                if ACTIVE_SCREEN == PLAY:
                    ACTIVE_SCREEN = SETTINGS
            if guihelpers.cursor_on_text_box(LOAD_X, LOAD_Y, LOAD_T, BUTTON_FONT):
                if ACTIVE_SCREEN == PLAY:
                    ACTIVE_SCREEN = LOAD
                else:
                    game.board = copy.deepcopy(loader.states[loader.cursor])
                    ACTIVE_SCREEN = PLAY

    # Asetetaan se taustavariksi
    screen.fill(BLACK)

    if ACTIVE_SCREEN == PLAY:
        game.tick(screen, events, loader, options)
    if ACTIVE_SCREEN == LOAD:
        loader.tick(screen, events, options)
    if ACTIVE_SCREEN == SETTINGS:
        options.tick(screen, events)

    # piirra!
    pygame.display.flip()

loader.save()
pygame.quit()
