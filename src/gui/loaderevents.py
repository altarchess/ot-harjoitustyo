import pygame
import entity.fileutil
import gui.externalboard
import gui.externalloader
import gui.guihelpers as guihelpers
from defs import *

class LoaderEvents:
    def __init__(self):
        self.loader = entity.fileutil.Loader()

    def tick(self, screen, events, options):
        gui.externalboard.render(
            screen, options, self.loader.states[self.loader.cursor])
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if guihelpers.cursor_on_text_box(PREVIOUS_X, PREVIOUS_Y, PREVIOUS_T, BUTTON_FONT):
                    self.loader.inc_cursor()

                if guihelpers.cursor_on_text_box(NEXT_X, NEXT_Y, NEXT_T, BUTTON_FONT):
                    self.loader.dec_cursor()

        gui.externalloader.render(screen)