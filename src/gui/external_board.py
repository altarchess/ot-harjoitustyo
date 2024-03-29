import pygame
from misc.defs import *
from entity.internal_board import *
import engine.move_gen
from gui import gui_helpers


def render(screen, options, board):
    """
    funktio othello laudan piirtoa varten

    Args:
        screen: pygame ruutu
        options: asetukset, kuten listattu entity.settings.Settings luokassa
        board: othello-lauta objekti joka halutaan pirtaa
    """

    # piirra tausta
    pygame.draw.rect(screen, GREEN, (X_OFFSET, Y_OFFSET,
                                     CELL_SIZE * COLUMNS, CELL_SIZE * ROWS))

    # Piirra ruudukko
    for i in range(COLUMNS + 1):
        pygame.draw.line(screen, DARK_GREEN, (X_OFFSET,  Y_OFFSET + CELL_SIZE * i),
                         (X_OFFSET + CELL_SIZE * COLUMNS,  Y_OFFSET + CELL_SIZE * i), 5)
        pygame.draw.line(screen, DARK_GREEN, (X_OFFSET + CELL_SIZE * i, Y_OFFSET),
                         (X_OFFSET + CELL_SIZE * i, Y_OFFSET + CELL_SIZE * ROWS), 5)

    # Piirra siirtovuoronappula
    if board.get_active_player() == WHITE_PIECE:
        pygame.draw.circle(
            screen, WHITE, (X_OFFSET + CELL_SIZE * COLUMNS, Y_OFFSET + CELL_SIZE * ROWS), 4)
    else:
        pygame.draw.circle(
            screen, BLACK, (X_OFFSET + CELL_SIZE * COLUMNS, Y_OFFSET + CELL_SIZE * ROWS), 4)

    for x in range(COLUMNS):
        for y in range(ROWS):
            if board.get_piece_on_square(y * COLUMNS + x) == 0:
                pass
            elif board.get_piece_on_square(y * COLUMNS + x) == WHITE_PIECE:
                pygame.draw.circle(screen, WHITE, (X_OFFSET + x * CELL_SIZE + CELL_SIZE /
                                                   2, Y_OFFSET + y * CELL_SIZE + CELL_SIZE / 2), PIECE_SIZE)
            elif board.get_piece_on_square(y * COLUMNS + x) == BLACK_PIECE:
                pygame.draw.circle(screen, BLACK, (X_OFFSET + x * CELL_SIZE + CELL_SIZE /
                                                   2, Y_OFFSET + y * CELL_SIZE + CELL_SIZE / 2), PIECE_SIZE)

    if options.settings.get_setting(SHOW_LEGAL) == "ON":
        gen = engine.move_gen.MoveGen()
        gen.generate(board)
        for move in gen.move_list:
            pygame.draw.circle(screen, GRAY, (X_OFFSET + x_from_square(move.start) * CELL_SIZE + CELL_SIZE /
                                              2, Y_OFFSET + y_from_square(move.start) * CELL_SIZE + CELL_SIZE / 2), PIECE_SIZE / 2)

    win_state = board.is_win()
    gui_helpers.draw_button(screen, WIN_X, WIN_Y, WINSTATES[win_state], gui_helpers.cursor_on_text_box(
        WIN_X, WIN_Y, WINSTATES[win_state], BUTTON_FONT))
