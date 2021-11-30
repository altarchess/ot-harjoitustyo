from copy import deepcopy
import pygame, othello, fileutil, helpers, copy
from defs import *

#luodaan ruutu
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Othello GUI") 

mode   = PLAY
board  = othello.Board()
loader = fileutil.Loader()
#ns. Pelilooppi.
running = True
while running: 
    #Tarkistetaan vain yrittaako kayttaja sulkea ohjelman.
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if helpers.cursorOnTextBox(LOAD_X, LOAD_Y, LOAD_T, BUTTON_FONT):
                if mode == PLAY:
                    mode = LOAD
                else:
                    board = copy.deepcopy(loader.states[loader.cursor])
                    mode = PLAY

    
    #Asetetaan se taustavariksi
    screen.fill(BLACK)

    if mode == PLAY:
        board.tick(screen, events, loader)
    if mode == LOAD:
        loader.tick(screen, events)

    #piirra!
    pygame.display.flip() 

loader.save()
pygame.quit() 