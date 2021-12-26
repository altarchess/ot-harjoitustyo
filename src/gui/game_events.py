import math
import pygame
from entity.internal_board import *
import gui.external_board
import engine.move_gen
import engine.ai
from gui import gui_helpers
from misc.defs import ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T
from misc.defs import SAVE_X, SAVE_Y, SAVE_T, LOAD_X, LOAD_Y, LOAD_T
from misc.defs import NEW_X, NEW_Y, NEW_T, OPTIONS_X, OPTIONS_T, OPTIONS_T
from misc.defs import BUTTON_FONT, CELL_SIZE, X_OFFSET, Y_OFFSET


class GameEvents:

    """
    Luokka kasittelee pelimoodissa tapahtumia

    Attributes:
        board: Lauta jota tapahtumat koskee
    """

    def __init__(self):
        self.board = Board()

    def tick(self, screen, events, loader, options):
        """
        Jokaisen ruudun piiroksen aikana kasitellaan hiirinappauspainallukset 
        mikali painetaan jotain nappulaa tai halutaa tehda siirto. 
        funktio myos pirtaa othello-laudan.

        Args:
            screen: pygame ruutu johon lauta halutaan pirtaa
            events: pygamen tapahtumat joita kasitellaan
            loader: kaytossa oleva asemien lataaja. Tarvitaan Mikali kayttaja haluaa tallentaa aseman
            options: Laudan ja AI:n asetukset
        """

        gui.external_board.render(screen, options, self.board)

        gui_helpers.draw_button(screen, ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T, gui_helpers.cursor_on_text_box(
            ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T, BUTTON_FONT))
        gui_helpers.draw_button(screen, SAVE_X, SAVE_Y, SAVE_T, gui_helpers.cursor_on_text_box(
            SAVE_X, SAVE_Y, SAVE_T, BUTTON_FONT))
        gui_helpers.draw_button(screen, NEW_X, NEW_Y, NEW_T, gui_helpers.cursor_on_text_box(
            NEW_X, NEW_Y, NEW_T, BUTTON_FONT))
        gui_helpers.draw_button(screen, LOAD_X, LOAD_Y, LOAD_T, gui_helpers.cursor_on_text_box(
            LOAD_X, LOAD_Y, LOAD_T, BUTTON_FONT))
        gui_helpers.draw_button(screen, OPTIONS_X, OPTIONS_Y, OPTIONS_T, gui_helpers.cursor_on_text_box(
            OPTIONS_X, OPTIONS_Y, OPTIONS_T, BUTTON_FONT))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                cord = pygame.mouse.get_pos()
                x = cord[0]
                y = cord[1]
                lauta_x = math.floor((x-X_OFFSET)/CELL_SIZE)
                lauta_y = math.floor((y-Y_OFFSET)/CELL_SIZE)
                if not (lauta_x >= COLUMNS or lauta_x < 0 or lauta_y >= ROWS or lauta_y < 0):
                    gen = engine.move_gen.MoveGen()
                    gen.generate(self.board)
                    for move in gen.move_list:
                        if move.start == square_from_xy(lauta_x, lauta_y):
                            self.board.make_move(move)
                if gui_helpers.cursor_on_text_box(ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T, BUTTON_FONT):
                    engine.ai.alpha_beta(options.settings.get_setting(AI_LEVEL),
                                         0, self.board, -10**19, 10**19)
                    if self.board.best_move != -1:
                        self.board.make_move(self.board.best_move)

                if gui_helpers.cursor_on_text_box(NEW_X, NEW_Y, NEW_T, BUTTON_FONT):
                    self.__init__()

                if gui_helpers.cursor_on_text_box(SAVE_X, SAVE_Y, SAVE_T, BUTTON_FONT):
                    loader.loader.add(self.board)
