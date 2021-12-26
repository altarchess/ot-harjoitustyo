import math
from defs import *
import engine.move_gen

# Auttaja funktiot


def x_from_square(square):
    return square % COLUMNS


def y_from_square(square):
    return math.floor(square/COLUMNS)


def square_from_xy(square_x, square_y):
    return square_x + square_y * COLUMNS

# Laudan luokka


class Board:

    def __init__(self):
        self.__piece_list = [0] * N_SQUARES
        self.__piece_list[D4] = BLACK_PIECE
        self.__piece_list[E4] = WHITE_PIECE
        self.__piece_list[D5] = WHITE_PIECE
        self.__piece_list[E5] = BLACK_PIECE
        self.__active_player = WHITE_PIECE
        self.best_move = 0  # temp value set by alpha_beta

    def set_piece(self, square, piece):
        self.__piece_list[square] = piece

    def get_piece_on_square(self, square):
        if square < 0 or square >= N_SQUARES:
            return 0
        return self.__piece_list[square]

    def get_piece_on_cord(self, x, y):
        if x >= COLUMNS or x < 0 or y >= ROWS or y < 0:
            return 0
        return self.__piece_list[y * ROWS + x]

    def get_active_player(self):
        return self.__active_player

    def make_move(self, move: engine.move_gen.Move):
        # We asume that the move is legal
        for i in range(move.steps):
            self.__piece_list[move.start + i * move.direction] = move.color
        self.__active_player = 0 - move.color

    def make_null_move(self):
        self.__active_player = 0 - self.__active_player

    def is_win(self):
        gen = engine.move_gen.MoveGen()
        gen.generate(self)
        if len(gen.move_list) == 0:
            self.__active_player = 0 - self.__active_player
            gen = engine.move_gen.MoveGen()
            gen.generate(self)
            if len(gen.move_list) == 0:
                score = 0
                for i in range(N_SQUARES):
                    score += self.get_piece_on_square(i)
                return 2 + max(-1, min(1, score))
            return ONGOING
        return ONGOING
