import math
import pygame
from defs import *
from othelloboard.internalboard import *
import othelloboard.externalboard
import engine.movegen
import engine.ai
import guihelpers


class GameEvents:
    def __init__(self):
        self.board = Board()

    def tick(self, screen, events, loader, options):
        othelloboard.externalboard.render(screen, options, self.board)

        guihelpers.draw_button(screen, ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T, guihelpers.cursor_on_text_box(
            ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T, BUTTON_FONT))
        guihelpers.draw_button(screen, SAVE_X, SAVE_Y, SAVE_T, guihelpers.cursor_on_text_box(
            SAVE_X, SAVE_Y, SAVE_T, BUTTON_FONT))
        guihelpers.draw_button(screen, NEW_X, NEW_Y, NEW_T, guihelpers.cursor_on_text_box(
            NEW_X, NEW_Y, NEW_T, BUTTON_FONT))
        guihelpers.draw_button(screen, LOAD_X, LOAD_Y, LOAD_T, guihelpers.cursor_on_text_box(
            LOAD_X, LOAD_Y, LOAD_T, BUTTON_FONT))
        guihelpers.draw_button(screen, OPTIONS_X, OPTIONS_Y, OPTIONS_T, guihelpers.cursor_on_text_box(
            OPTIONS_X, OPTIONS_Y, OPTIONS_T, BUTTON_FONT))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                cord = pygame.mouse.get_pos()
                x = cord[0]
                y = cord[1]
                lauta_x = math.floor((x-X_OFFSET)/CELL_SIZE)
                lauta_y = math.floor((y-Y_OFFSET)/CELL_SIZE)
                if not (lauta_x >= COLUMNS or lauta_x < 0 or lauta_y >= ROWS or lauta_y < 0):
                    gen = engine.movegen.MoveGen()
                    gen.generate(self.board)
                    for move in gen.move_list:
                        if move.start == square_from_xy(lauta_x, lauta_y):
                            self.board.make_move(move)
                if guihelpers.cursor_on_text_box(ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T, BUTTON_FONT):
                    engine.ai.alpha_beta(options.get_setting(AI_LEVEL),
                                         0, self.board, -10**19, 10**19)
                    if self.board.best_move != -1:
                        self.board.make_move(self.board.best_move)

                if guihelpers.cursor_on_text_box(NEW_X, NEW_Y, NEW_T, BUTTON_FONT):
                    self.__init__()

                if guihelpers.cursor_on_text_box(SAVE_X, SAVE_Y, SAVE_T, BUTTON_FONT):
                    loader.add(self.board)