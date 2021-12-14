from copy import deepcopy
import copy
import pygame
import othello
import fileutil
import helpers
import settings
from defs import *

# luodaan ruutu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Othello GUI")

mode = PLAY
board    = othello.Board()
loader   = fileutil.Loader()
options  = settings.Settings()
# ns. Pelilooppi.
running = True
while running:
    # Tarkistetaan vain yrittaako kayttaja sulkea ohjelman.
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:    
            if helpers.cursor_on_text_box(ENGINE_MOVE_X, ENGINE_MOVE_Y, "Go Back", BUTTON_FONT):
                if mode == SETTINGS:
                    mode = PLAY
            if helpers.cursor_on_text_box(OPTIONS_X, OPTIONS_Y, OPTIONS_T, BUTTON_FONT):
                if mode == PLAY:
                    mode = SETTINGS
            if helpers.cursor_on_text_box(LOAD_X, LOAD_Y, LOAD_T, BUTTON_FONT):
                if mode == PLAY:
                    mode = LOAD
                else:
                    board = copy.deepcopy(loader.states[loader.cursor])
                    mode = PLAY

    # Asetetaan se taustavariksi
    screen.fill(BLACK)

    if mode == PLAY:
        board.tick(screen, events, loader, options)
    if mode == LOAD:
        loader.tick(screen, events)
    if mode == SETTINGS:
        options.tick(screen, events)

    # piirra!
    pygame.display.flip()

loader.save()
pygame.quit()
