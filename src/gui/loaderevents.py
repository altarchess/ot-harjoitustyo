import pygame
import entity.file_util
import gui.external_board
import gui.external_loader
from gui import guihelpers
from defs import PREVIOUS_X, PREVIOUS_Y, PREVIOUS_T, BUTTON_FONT, NEXT_X, NEXT_Y, NEXT_T

class LoaderEvents:
    def __init__(self):
        self.loader = entity.file_util.Loader()

    def tick(self, screen, events, options):
        gui.external_board.render(
            screen, options, self.loader.states[self.loader.cursor])
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if guihelpers.cursor_on_text_box(PREVIOUS_X, PREVIOUS_Y, PREVIOUS_T, BUTTON_FONT):
                    self.loader.inc_cursor()

                if guihelpers.cursor_on_text_box(NEXT_X, NEXT_Y, NEXT_T, BUTTON_FONT):
                    self.loader.dec_cursor()

        gui.external_loader.render(screen)
