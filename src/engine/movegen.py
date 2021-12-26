import copy
import othelloboard.internalboard
from defs import *


class MoveGen:
    def __init__(self):
        self.move_list = []

    def slider(self, board, square, direction):
        square_x = othelloboard.internalboard.x_from_square(square)
        square_y = othelloboard.internalboard.y_from_square(square)
        xmod = 0
        ymod = 0

        if direction in (NW, N, NE):
            ymod += 1
        if direction in (SW, S, SE):
            ymod -= 1
        if direction in (NE, E, SE):
            xmod += 1
        if direction in (NW, W, SW):
            xmod -= 1

        steps = 0
        while True:
            steps += 1
            square_x += xmod
            square_y += ymod
            piece = board.get_piece_on_cord(square_x, square_y)
            if piece == EMPTY_PIECE:
                return Move(-1, 0, 0, EMPTY_PIECE)
            if piece == board.get_active_player():
                if steps > 1:
                    return Move(square, steps, xmod + ymod * COLUMNS, board.get_active_player())
                return Move(-1, 0, 0, EMPTY_PIECE)

    def generate(self, board):
        for i in range(N_SQUARES):
            if (board.get_piece_on_square(i) == EMPTY_PIECE):
                # Jos ruutu on tyhja, tarkista onko siirto ruutuun mahdollinen tarkistamalla eri suunnassa olevat nappulat.
                for dir in range(DIRECTIONS):
                    m = self.slider(board, i, dir)
                    if m.steps > 0:
                        self.move_list.append(m)

# Siirto luokka


class Move:
    def __init__(self, start, steps, direction, color):
        self.start = start
        self.steps = steps
        self.direction = direction
        self.color = color
